# more_info.py
import streamlit as st
from pathlib import Path
from PIL import Image
# -----------------------------
# Page configuration
# -----------------------------
st.set_page_config(
    page_title="About Rabbit - Company Info",
    page_icon="🐇",
    layout="wide",
)
# -----------------------------
# CSS Styling for Background & Sections
# -----------------------------
st.markdown("""
<style>
/* Background Image for the page */
.stApp {
    background-image: url('https://images.unsplash.com/photo-1556761175-129418cb2dfe?auto=format&fit=crop&w=1350&q=80');
    background-size: cover;
    background-attachment: fixed;
    background-position: center;
    color: #ffffff;
}

/* Section styling */
.company-section {
    background-color: rgba(0, 0, 0, 0.6);
    padding: 30px;
    border-radius: 15px;
    margin-bottom: 20px;
}

/* Partner logos section */
.partner {
    background-color: rgba(255, 255, 255, 0.1);
    padding: 15px;
    border-radius: 10px;
    text-align: center;
    margin: 10px;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# Company Header
# -----------------------------
st.markdown("""
<div class="company-section" style="text-align:center;">
    <h1 style="font-size:60px; font-family: 'Trebuchet MS', sans-serif;">🐇 Rabbit</h1>
    <h3 style="font-family: 'Arial', sans-serif;">Delivering software solutions to scale marketing sectors for businesses</h3>
    <p>Founded by <strong>Mr. Ruturaj</strong> with a strong market base of <strong>10,000+ employees</strong></p>
</div>
""", unsafe_allow_html=True)

# -----------------------------
# Company Description
# -----------------------------
st.markdown("""
<div class="company-section">
    <h2>About Rabbit</h2>
    <p>
        Rabbit is a service-based organisation dedicated to providing innovative software solutions
        that empower businesses in the marketing sector. With a professional yet creative approach,
        we focus on scaling the growth of our partners and clients across diverse industries.
    </p>
    <p>
        Being a large-cap company, Rabbit maintains a strong market hold and is recognized for
        its consistent performance and growth in the tech and software sector.
    </p>
</div>
""", unsafe_allow_html=True)

# -----------------------------
# Business Partners
# -----------------------------
import streamlit as st
from pathlib import Path
from PIL import Image, UnidentifiedImageError

# ensure BASE_DIR is defined (safe default)
BASE_DIR = Path(__file__).resolve().parent
ASSETS = BASE_DIR.parent / "images"
partners = {
    "Zepto Corporation": "zepto.png",
    "Alpha Corporation": "alpha.png",
    "Omega Solutions": "omega.png",
    "Delta Enterprises": "delta.png",
}
cols = st.columns(len(partners))
for col, (name, fname) in zip(cols, partners.items()):
    img_path = (ASSETS / fname).resolve() if ASSETS.exists() else None
    col.subheader(name)
    if img_path and img_path.exists():
        try:
            # quick integrity check
            img = Image.open(img_path)
            img.verify()  # raises if file is bad
            # reopen for display (verify() closes file)
            img = Image.open(img_path)
            col.image(img, caption=f"{name} — {img_path.name}", use_container_width=True)
        except UnidentifiedImageError:
            col.error(f"File found but not a valid image: {img_path}")
        except Exception as e:
            col.error(f"Error opening image {img_path}: {e}")
    else:
        col.error(f"Image not found at: {img_path if img_path else ASSETS}")
# -----------------------------
# Market Info Section
# -----------------------------
st.markdown("""
<div class="company-section">
    <h2>Market Presence</h2>
    <p>
        Rabbit is recognized as a leader in the software solutions sector. Our large-cap status and
        robust market performance make us a trusted partner for businesses looking to innovate and scale.
    </p>
</div>
""", unsafe_allow_html=True)
# -----------------------------
# Footer
# -----------------------------
st.markdown("""
<footer style="text-align:center; padding:10px; margin-top:20px; background-color: rgba(0,0,0,0.6); border-radius:10px;">
    <p>© 2025 Rabbit Corporation. All rights reserved.</p>
</footer>
""", unsafe_allow_html=True)