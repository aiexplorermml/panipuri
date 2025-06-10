import streamlit as st
import base64
from pathlib import Path

# Set page config
st.set_page_config(
    page_title="Pani-Puri Defender",
    page_icon="🍘",
    layout="centered",
    initial_sidebar_state="collapsed"
)

def get_base64_encoded_file(file_path):
    """Return base64 encoded file"""
    with open(file_path, "rb") as f:
        return base64.b64encode(f.read()).decode('utf-8')

def main():
    st.title("Pani-Puri Defender 🍘")
    st.markdown("""
    ### Protect your Pani-Puri stall from evil samosas!
    Move your finger/mouse to control the chef and tap to shoot puris.
    """)
    
    # Load HTML file
    html_file = Path(__file__).parent / "index.html"
    
    if html_file.exists():
        with open(html_file, "r", encoding="utf-8") as f:
            html_content = f.read()
        
        # Display the game
        st.components.v1.html(html_content, height=800, scrolling=True)
    else:
        st.error("Game file not found. Please make sure index.html exists in the same directory.")

if __name__ == "__main__":
    main()
