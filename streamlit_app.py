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
    
    # Add some game instructions
    with st.expander("How to Play"):
        st.markdown("""
        - Use your mouse or finger to move the chef left and right
        - Click or tap to shoot puris at the incoming samosas
        - Don't let the samosas reach your stall!
        - Score points for each samosa you hit
        """)
    
    # Add a high scores section
    st.sidebar.title("High Scores")
    st.sidebar.write("Coming soon...")
    
    # Load HTML file
    html_file = Path(__file__).parent / "puri.html"
    
    if html_file.exists():
        with open(html_file, "r", encoding="utf-8") as f:
            html_content = f.read()
        
        # Display the game with a nicer border
        st.markdown("---")
        st.components.v1.html(html_content, height=600, scrolling=False)
        st.markdown("---")
        
        # Add a restart button
        if st.button("Restart Game"):
            st.experimental_rerun()
    else:
        st.error("Game file not found. Please make sure index.html exists in the same directory.")
        
    # Footer
    st.markdown("""
    ---
    Made with ❤️ by Pani-Puri lovers everywhere
    """)

if __name__ == "__main__":
    main()
