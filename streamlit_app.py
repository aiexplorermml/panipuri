import streamlit as st
from pathlib import Path

# Set page config
st.set_page_config(
    page_title="Pani-Puri Defender",
    page_icon="🍘",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Function to read the HTML file
def read_html_file():
    # Get the path to the HTML file (assuming it's in the same directory)
    html_path = Path(__file__).parent / "index.html"
    with open(html_path, "r", encoding="utf-8") as f:
        return f.read()

# Main app
def main():
    st.title("Pani-Puri Defender 🍘")
    st.markdown("""
    ### Protect your Pani-Puri stall from evil samosas!
    Move your finger/mouse to control the chef and tap to shoot puris.
    """)
    
    # Display the game
    html_content = read_html_file()
    st.components.v1.html(html_content, height=800, scrolling=True)

if __name__ == "__main__":
    main()
