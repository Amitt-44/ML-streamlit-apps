import streamlit as st
import requests
import io
from PIL import Image

API_URL = "https://api-inference.huggingface.co/models/black-forest-labs/FLUX.1-dev"
headers = {"Authorization": "Bearer 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"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    if response.status_code == 200:
        return response.content
    else:
        st.error(f"Error: {response.status_code} - {response.text}")
        return None

# Streamlit UI setup
st.set_page_config(page_title="Image Generator", layout="wide")
st.title("🪐Image generator model")
st.markdown(
    "Create stunning images of astronauts riding horses using a AI!"
)
st.sidebar.header("Settings")

# Input text for image generation
user_input = st.text_input("Enter a description:", "Astronaut riding a horse")
num_images = st.slider("Number of images to generate:", 1, 5, 1)

if st.button("Generate Image"):
    with st.spinner("Generating images..."):
        images = []
        for _ in range(num_images):
            image_bytes = query({"inputs": user_input})
            if image_bytes:  # Check if image_bytes is not None
                try:
                    image = Image.open(io.BytesIO(image_bytes))
                    images.append(image)
                except Exception as e:
                    st.error(f"Failed to process image: {e}")
        
        # Display the images if any were generated successfully
        if images:
            st.success("Images generated successfully!")
            for img in images:
                st.image(img, caption=user_input, use_column_width=True)

# Footer
st.markdown("---")
st.markdown("### ")

st.markdown("Made with ❤️ ")

# CSS for customization
st.markdown(
    """
    <style>
    .stButton > button {
        background-color: #4CAF50; /* Green */
        color: white;
        padding: 15px 32px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 12px;
    }
    .stTextInput > div > input {
        border-radius: 12px;
        padding: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
