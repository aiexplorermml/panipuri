import streamlit as st
from pathlib import Path

# Set up the page
st.set_page_config(
    page_title="Pani-Puri Defender",
    page_icon="🍘",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Simple title and instructions
st.title("Pani-Puri Defender 🍘")
st.markdown("Shoot puris to protect your stall from samosas! 👆🍽️")

# Load and display the game HTML
try:
    html = Path("puri.html").read_text()
    st.components.v1.html(html, width=600, height=600, scrolling=False,layout="centered",)
except:
    st.error("Game file (puri.html) not found in the same directory")

# Footer
st.markdown("---")
st.caption("Made with ❤️ by Pani-Puri lovers")
