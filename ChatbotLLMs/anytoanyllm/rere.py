import requests

API_URL = "https://api-inference.huggingface.co/models/gpt2"
headers = {"Authorization": "Bearer YOUR_API_TOKEN"}

def generate_poem(prompt, max_length=100):
    payload = {
        "inputs": prompt,
        "parameters": {
            "max_length": max_length,
            "num_return_sequences": 1,
            "temperature": 0.9,  # Higher temperature for more creativity
        }
    }
    response = requests.post(API_URL, headers=headers, json=payload)
    if response.status_code == 200:
        return response.json()[0]['generated_text']
    else:
        return f"Error: {response.status_code} - {response.text}"

# Example usage
prompt = "In the quiet of the night,"
poem = generate_poem(prompt)
print(poem)
