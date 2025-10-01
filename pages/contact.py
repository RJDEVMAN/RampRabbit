# contact_us.py
import streamlit as st

# Page config
st.set_page_config(
    page_title="Contact Us - Rabbit",
    page_icon="📞",
    layout="centered"
)
st.title("📬 Contact Us")
st.write("Reach out to us for any queries or support regarding Rabbit's services!")
# -----------------------------
# Contact Cards
# -----------------------------
st.markdown("""
<style>
.contact-card {
    background-color: #f0f8ff;
    border: 1px solid #c0c0c0;
    border-radius: 12px;
    padding: 20px;
    max-width: 450px;
    margin-bottom: 20px;
    box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
}
.contact-name {
    font-size: 18px;
    font-weight: bold;
    color: #333333;
    margin-bottom: 5px;
}
.contact-info {
    font-size: 16px;
    margin-bottom: 8px;
}
.contact-info a {
    color: #1a73e8;
    text-decoration: none;
}
.contact-info a:hover {
    text-decoration: underline;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# General Contact
# -----------------------------
st.markdown("""
<div class="contact-card">
    <div class="contact-name">General Enquiries</div>
    <div class="contact-info"><b>Phone:</b> +91 1234567890</div>
    <div class="contact-info"><b>Email:</b> <a href="mailto:RJ@example.com">RJ@example.com</a></div>
    <div class="contact-info"><b>Address:</b> Rabbit Corporation, 123 Tech Avenue, Mumbai, India</div>
</div>
""", unsafe_allow_html=True)

# -----------------------------
# Software Manager Contact
# -----------------------------
st.markdown("""
<div class="contact-card">
    <div class="contact-name">Software Manager</div>
    <div class="contact-info"><b>Phone:</b> +91 9876543210</div>
    <div class="contact-info"><b>Email:</b> <a href="mailto:sm.rabbit@example.com">sm.rabbit@example.com</a></div>
    <div class="contact-info"><b>Office:</b> Rabbit Tech HQ, Room 405</div>
</div>
""", unsafe_allow_html=True)

# -----------------------------
# Footer
# -----------------------------
st.markdown("""
<div style="text-align:center; font-size:14px; color:#555; margin-top:30px;">
    Made with 💖 by RJ | Rabbit Corporation
</div>
""", unsafe_allow_html=True)
