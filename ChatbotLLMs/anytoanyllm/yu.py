import streamlit as st
import requests
import io
from PIL import Image
import numpy as np

# API URLs for different models (update these with correct URLs)
API_URLS = {
    "text_to_image": "https://api-inference.huggingface.co/models/black-forest-labs/FLUX.1-dev",
    "text_generation": "https://api-inference.huggingface.co/models/openai-community/gpt2",
    "image_to_image": "",
    "text_to_speech": "https://api-inference.huggingface.co/models/MIT/ast-finetuned-audioset-10-10-0.4593",
}

# Replace with your actual token
headers = {"Authorization": "Bearer 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"}

def query(api_url, payload):
    response = requests.post(api_url, headers=headers, json=payload)
    if response.status_code == 200:
        return response.content
    else:
        st.error(f"Error: {response.status_code} - {response.text}")
        return None

# Streamlit UI setup
st.set_page_config(page_title="Creative AI Generator", layout="wide")
st.title("🎨 Creative AI Generator")
st.markdown("Choose a feature from the sidebar to get started! 🚀")

# Sidebar for model selection
st.sidebar.header("Select Functionality")
model_selection = st.sidebar.radio("Choose a feature:", [
    "Text to Image",
    "Text Generation",
    "Image to Image",
    "Text to Speech",
    "Image to Video"  # Placeholder for future functionality
])

# Text to Image
if model_selection == "Text to Image":
    st.subheader("🖼️ Text to Image")
    user_input = st.text_input("Enter a description:", "Astronaut riding a horse")
    if st.button("Generate Image"):
        with st.spinner("Generating image..."):
            image_bytes = query(API_URLS["text_to_image"], {"inputs": user_input})
            if image_bytes:
                image = Image.open(io.BytesIO(image_bytes))
                st.image(image, caption=user_input, use_column_width=True)

# Text Generation
elif model_selection == "Text Generation":
    st.subheader("✍️ Text Generation")
    user_input = st.text_area("Enter your prompt:", "Once upon a time...")
    if st.button("Generate Text"):
        with st.spinner("Generating text..."):
            response = query(API_URLS["text_generation"], {"inputs": user_input})
            if response:
                generated_text = response.decode('utf-8')
                st.text_area("Generated Text:", generated_text, height=200)

# Image to Image
elif model_selection == "Image to Image":
    st.subheader("🖼️ Image to Image")
    uploaded_file = st.file_uploader("Upload an image:", type=["png", "jpg", "jpeg"])
    if uploaded_file is not None:
        st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
        if st.button("Transform Image"):
            with st.spinner("Transforming image..."):
                # Placeholder for image transformation logic
                st.success("Image transformed successfully!")

# Text to Speech
elif model_selection == "Text to Speech":
    st.subheader("🔊 Text to Speech")
    text_input = st.text_input("Enter text to convert to speech:", "Hello, how are you?")
    if st.button("Generate Speech"):
        with st.spinner("Generating speech..."):
            audio_bytes = query(API_URLS["text_to_speech"], {"inputs": text_input})
            if audio_bytes:
                st.audio(audio_bytes, format="audio/wav")

# Image to Video
elif model_selection == "Image to Video":
    st.subheader("📽️ Image to Video")
    st.info("This feature is under development! Stay tuned for updates!")

# Footer
st.markdown("---")
st.markdown("### About")
st.markdown("This app uses various Hugging Face models to create amazing content.")
st.markdown("Made with ❤️ by [Your Name]")

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
    .stTextInput > div > input,
    .stTextArea > div > textarea {
        border-radius: 12px;
        padding: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
