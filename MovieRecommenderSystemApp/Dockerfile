# Use a lightweight Python image
FROM python:3.8-slim

# Set the working directory
WORKDIR /MovieRecommenderSystemApp/app.py

# Copy requirements.txt into the container
COPY requirements.txt .

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code
COPY . .

# Expose the port for the Streamlit app
EXPOSE 8501

# Command to run the Streamlit app
CMD ["streamlit", "run", "main.py"]

