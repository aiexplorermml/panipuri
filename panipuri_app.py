import streamlit as st
from pathlib import Path

# Page setup
st.set_page_config(
    page_title="Pani-Puri Defender",
    page_icon="🍘",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Title and header
st.markdown("<h1 style='text-align: center;'>Pani-Puri Defender 🍘</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Shoot puris to protect your stall from samosas! 👆🍽️</p>", unsafe_allow_html=True)

# Scoreboard (placeholder for future interaction)
st.markdown("### Score: 0")  # You can link this to JavaScript via query param / JS bridge later

# Start game button
if st.button("🎮 Start Game"):
    st.success("Game started! Focus on the game window below.")

# Load and display the HTML game
try:
    html = Path("puri.html").read_text()

    # Wrap HTML inside a div for centering
    styled_html = f"""
    <div style="display: flex; justify-content: center;">
        <div style="width: 600px; height: 800px; border: 2px solid #FACC15; border-radius: 12px; overflow: hidden;">
            {html}
        </div>
    </div>
    """

    st.components.v1.html(styled_html, height=820, scrolling=False)

except FileNotFoundError:
    st.error("Game file (puri.html) not found in the current directory.")

# Footer
st.markdown("---")
st.caption("Made with ❤️ by Pani-Puri lovers")
