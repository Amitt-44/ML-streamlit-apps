import streamlit as st
import numpy as np
import cv2
from tensorflow import keras
from PIL import Image
from streamlit_drawable_canvas import st_canvas  # Import st_canvas

# Load your trained model
model = keras.models.load_model(r'digit_recognition_webapp/classifier.keras')

# Set page title and icon
st.set_page_config(page_title="Digit Recognizer", page_icon=":1234:")

# Define function to preprocess the image
def preprocess_image(img):
    img = img.resize((28, 28))  # Resize to match model input shape
    img = img.convert('L')  # Convert to grayscale
    img_array = np.array(img)  # Convert to numpy array
    img_array = img_array / 255.0  # Normalize pixel values
    img_array = img_array.reshape(1, 28, 28, 1)  # Reshape for model input
    return img_array

# Define prediction function
def predict_digit(img):
    processed_img = preprocess_image(img)
    prediction = model.predict(processed_img)
    digit = np.argmax(prediction)
    return digit

# Create Streamlit UI
st.title("Handwritten Digit Recognition")
st.write("Draw a digit in the box below and click 'Predict'")

# Create a canvas for drawing
canvas_result = st_canvas(
    fill_color="rgba(255, 165, 0, 0.3)",  # Set canvas fill color
    stroke_width=10,
    stroke_color="#000000",
    background_color="#FFFFFF",
    update_streamlit=True,
    height=200,
    width=200,
    drawing_mode="freedraw",
    key="canvas",
)

# Add a 'Predict' button
if st.button("Predict"):
    if canvas_result.image_data is not None:
        img = Image.fromarray(canvas_result.image_data.astype('uint8'), mode="RGBA")
        digit = predict_digit(img)

        # Display prediction with styling
        st.markdown(f"<h2 style='text-align: center; color: green;'>Prediction: {digit}</h2>", unsafe_allow_html=True) 
    else:
        st.warning("Please draw a digit on the canvas.")

# Add some styling
st.markdown(
    """
    <style>
    .stApp {
        background-color: #f0f2f6; /* Light gray background */
    }
    .stButton>button {
        background-color: #4CAF50; /* Green button */
        color: white;
        border: none;
        padding: 10px 20px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 5px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
