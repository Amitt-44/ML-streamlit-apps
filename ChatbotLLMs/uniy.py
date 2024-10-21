import streamlit as st
import requests

# Function to fetch predictions from the selected LLM model
def get_llm_response(prompt, model, api_key):
    url = f"https://api.unify.ai/v0/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}]
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json()

# Streamlit UI components
st.title("Unify AI LLM Selector")

# User input for API key
api_key = st.text_input("Enter your API key", type="password")

# Dropdown for selecting LLM models
models = ["gpt-3.5-turbo", "gpt-4", "other_model_name"]  # Add the model names you want to include
selected_model = st.selectbox("Choose a LLM model", models)

# User input for the prompt
prompt = st.text_area("Enter your prompt")

# Button to get response
if st.button("Get Response"):
    if api_key and prompt:
        response = get_llm_response(prompt, selected_model, api_key)
        st.json(response)
    else:
        st.warning("Please enter your API key and a prompt.")
