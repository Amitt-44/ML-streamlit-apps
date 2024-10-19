import streamlit as st
import pandas as pd

# Load the trained model
model = joblib.load('churn_model.pkl')

# Title of the app
st.title('Customer Churn Prediction App')

# User input fields
age = st.number_input('Age', min_value=18, max_value=100)
annual_income = st.number_input('Annual Income (USD)', min_value=1000, max_value=200000)
purchase_amount = st.number_input('Total Purchase Amount (USD)')
purchase_frequency = st.number_input('Purchase Frequency (Times per Year)')

# Create a button for prediction
if st.button('Predict Churn'):
    # Prepare input data
    input_data = pd.DataFrame({
        'age': [age],
        'annual_income': [annual_income],
        'purchase_amount': [purchase_amount],
        'purchase_frequency': [purchase_frequency]
    })
    
     #Make prediction
    prediction = model.predict(input_data)
    
    # Display prediction result
    if prediction[0] == 1:
        st.success('Customer is likely to churn.')
    else:
        st.success('Customer is not likely to churn.')
