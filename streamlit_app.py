import streamlit as st
from pathlib import Path
import os

# Set page config
st.set_page_config(
    page_title="Pani-Puri Defender",
    page_icon="🍘",
    layout="centered",
    initial_sidebar_state="collapsed"
)

def main():
    st.title("Pani-Puri Defender �")
    st.markdown("""
    ### Protect your Pani-Puri stall from evil samosas! 😊
    Move your finger/mouse to control the chef and tap to shoot puris.
    """)
    
    # How to Play section
    with st.expander("How to Play"):
        st.markdown("""
        - ← → Move the chef with mouse/finger
        - 🖱️ Click/Tap to shoot puris
        - 💥 Hit samosas to score points
        - ❌ Don't let samosas reach your stall!
        """)
    
    # Game container
    st.markdown("---")
    game_container = st.empty()
    st.markdown("---")
    
    # Check for HTML file
    html_file = Path(__file__).parent / "puri.html"
    
    if html_file.exists():
        try:
            with open(html_file, "r", encoding="utf-8") as f:
                html_content = f.read()
            game_container.components.v1.html(html_content, height=600, scrolling=False)
        except Exception as e:
            st.error(f"Error loading game: {str(e)}")
    else:
        st.error("""
        Game file not found. Please make sure:
        1. index.html exists in the same directory
        2. The file is named exactly 'index.html'
        3. All game assets are in an 'assets' folder
        """)
        st.info("Create a basic game file by running this in your terminal:")
        st.code("echo '<h1>Game coming soon!</h1>' > index.html", language="bash")

    # Footer
    st.markdown("""
    ---
    **Made with ❤️ by Pani-Puri lovers everywhere**
    """)

if __name__ == "__main__":
    main()
