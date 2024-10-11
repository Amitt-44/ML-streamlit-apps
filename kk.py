import streamlit as st
import numpy as np
import pandas as pd
import joblib

# Function to calculate EMI
def calculate_emi(principal, annual_rate, tenure_months):
    monthly_rate = annual_rate / 100 / 12
    emi = (principal * monthly_rate * (1 + monthly_rate) ** tenure_months) / ((1 + monthly_rate) ** tenure_months - 1)
    return emi

# Load the pre-trained machine learning model
def load_model():
    model = joblib.load('savings_model.pkl')
    return model

# Function to evaluate repayment strategy using ML model
def evaluate_with_ml_model(model, loan_amount, interest_rate, tenure, lump_sum, monthly_investment):
    emi_increase_fraction = 0.4  # This can be user-defined
    principal_repayment_fraction = 0.4  # This can be user-defined

    features = np.array([[loan_amount, interest_rate, tenure, monthly_investment, lump_sum, emi_increase_fraction, principal_repayment_fraction]])
    
    predicted_savings = model.predict(features)[0]
    
    return predicted_savings

# Streamlit App
st.title("Loan Repayment Optimization")

# User Inputs
loan_amount = st.number_input("Enter your loan amount:", min_value=10000, step=1000)
interest_rate = st.number_input("Enter the annual interest rate (in %):", min_value=1.0, max_value=30.0, step=0.1)
remaining_years = st.number_input("Enter the remaining loan tenure (in years):", min_value=1, step=1)
monthly_investment = st.number_input("Enter your monthly investment contribution:", min_value=0, step=100)
lump_sum = st.number_input("Enter your total savings available:", min_value=0, step=1000)

# Convert tenure to months
tenure = remaining_years * 12

# Load ML model
model = load_model()

# Calculate current EMI
current_emi = calculate_emi(loan_amount, interest_rate, tenure)

# Display current EMI
st.subheader("Current EMI Calculation")
st.write(f"Your current EMI is: ₹{current_emi:.2f}")

# Use the ML model to evaluate the repayment strategy
if st.button("Evaluate Savings"):
    predicted_savings = evaluate_with_ml_model(model, loan_amount, interest_rate, tenure, lump_sum, monthly_investment)
    st.subheader("Potential Savings")
    st.write(f"By optimizing your repayment strategy, you could save: ₹{predicted_savings:.2f}")

st.sidebar.title("Additional Options")
st.sidebar.write("Explore investment options and strategies to maximize wealth.")
# You can add more functionalities in the sidebar as needed

# Notes
st.markdown("## Notes")
st.write("This tool provides estimates based on your input data. Please consult a financial advisor for detailed analysis.")
