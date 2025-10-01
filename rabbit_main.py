import os
import numpy as np
import pickle
import streamlit as st
from dotenv import load_dotenv
from groq import Groq
from sentence_transformers import SentenceTransformer
from transformers import pipeline
import tempfile
import torch
import ffmpeg
# -----------------------------
# 1️⃣ Load API keys & models
# -----------------------------
load_dotenv()
client = Groq(api_key=st.secrets("GROQ_API_KEY"))
embed_model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2",
    use_auth_token=os.getenv("HF_TOKEN")
)
EMBEDDINGS_FILE = "company_data/embeddings.pkl"

# -----------------------------
# 2️⃣ Load precomputed embeddings
# -----------------------------
if os.path.exists(EMBEDDINGS_FILE):
    with open(EMBEDDINGS_FILE, "rb") as f:
        all_chunks, all_embeddings = pickle.load(f)
else:
    st.error("Embeddings file not found! Please generate embeddings first.")
    st.stop()

# -----------------------------
# 3️⃣ Streamlit UI
# -----------------------------
st.title("Welcome! I am CorpoRabbit 😊")
st.write("I can help you with queries regarding Rabbit's HR policies and company information.")
st.markdown(f"<img src='https://i.pinimg.com/originals/b6/e9/7d/b6e97d9c28651e1c05f91637334563a5.gif' width='260' loop='true'>", unsafe_allow_html=True)
user_query = st.text_input("Enter your query:")
final_query = None
if user_query.strip():
    final_query = user_query
if final_query is None:
    st.warning("Please provide a query via text!")
else:
    query_embedding = embed_model.encode([final_query], convert_to_numpy=True)[0]

# -----------------------------
# 4️⃣ Sidebar links and theme
# -----------------------------
# -----------------------------
# 4️⃣ Sidebar links and theme
# -----------------------------
st.sidebar.page_link("pages/contact.py", label="Contact us", icon="📞")
st.sidebar.page_link("pages/more_info.py", label="More information", icon="ℹ️")

# Theme toggle
import streamlit as st

is_dark = st.toggle("Dark mode", value=False)

if is_dark:
    bg_color = "#121212"
    fg_color = "white"
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-color: {bg_color};
            color: {fg_color};
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )
    st.write("Dark theme selected!")
else:
    bg_color = "white"
    fg_color = "black"
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-color: {bg_color};
            color: {fg_color};
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )
    st.write("Light theme selected!")

# -----------------------------
# 5️⃣ RAG: Retrieve & answer
# -----------------------------
if st.button("Send") and final_query:
    # Cosine similarity function
    def cosine_similarity(v1, v2):
        v1, v2 = np.array(v1), np.array(v2)
        if np.linalg.norm(v1) == 0 or np.linalg.norm(v2) == 0:
            return 0.0
        return float(np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2)))

    # Retrieve top-k chunks
    similarities = [cosine_similarity(query_embedding, emb) for emb in all_embeddings]
    top_k = 200
    top_idxs = sorted(range(len(similarities)), key=lambda i: similarities[i], reverse=True)[:top_k]
    retrieved_chunks = [all_chunks[i] for i in top_idxs] or ["No matching record found."]

    # Prepare prompt
    prompt_system = """
    You are CorpoRabbit, a helpful HR assistant for Rabbit company. 
    - Answer queries using *only* retrieved data. 
    - Do not hallucinate or provide partial info.
    - Cited: Every answer must include clear source references (e.g., “According to Employee Leaves policy..”)
    - Accurate: Synthesized using the most relevant documents.
    - Conversational: Do not just copy-paste your answers, keep the tone conversational and ask for any further help required to the user.
    - Display clear, user-friendly messages for missing data, upload failures, or model/API errors. 
    - Even you can tell user to provide any additional information, confusion,etc; he/she has and update your knowledge base accordingly.
    - Handle user input cases effectively, eg:- If user asks, 'How many types of leaves are there for HR Managers?', parse HR Managers as HR Manager and then search for the chunks.
    """

    prompt_user = f"""
    User query:
    {final_query}

    Retrieved record chunks:
    {retrieved_chunks}

    Answer based strictly on these chunks.
    For instructions, follow: {prompt_system}
    """
    # Call Groq LLM
    chat_completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": prompt_system},
            {"role": "user", "content": prompt_user},
        ],
        temperature=0.1,
        max_tokens=500,
    )
    answer = chat_completion.choices[0].message.content
    st.text_area("Response", value=answer, height=250)