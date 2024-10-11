import streamlit as st
import numpy as np
import pandas as pd

from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
import joblib

# Function to calculate EMI
def calculate_emi(principal, annual_rate, tenure_months):
    monthly_rate = annual_rate / 100 / 12
    emi = (principal * monthly_rate * (1 + monthly_rate) ** tenure_months) / ((1 + monthly_rate) ** tenure_months - 1)
    return emi

# Load or train the machine learning model
def load_model():
    try:
        model = joblib.load('savings_model.pkl')
    except FileNotFoundError:
        # Generate synthetic data if model not found (can be replaced with actual training)
        synthetic_data = generate_synthetic_data()
        model = train_model(synthetic_data)
    return model

# Generate synthetic dataset for model training
def generate_synthetic_data(num_samples=1000):
    data = {
        'loan_amount': np.random.randint(50000, 500000, size=num_samples),
        'interest_rate': np.random.uniform(5, 15, size=num_samples),
        'tenure_months': np.random.randint(12, 360, size=num_samples),
        'monthly_investment': np.random.randint(1000, 5000, size=num_samples),
        'lump_sum': np.random.randint(1000, 50000, size=num_samples),
        'emi_increase_fraction': np.random.uniform(0, 1, size=num_samples),
        'principal_repayment_fraction': np.random.uniform(0, 1, size=num_samples),
    }
    
    df = pd.DataFrame(data)
    df['principal_repayment_fraction'] = df['principal_repayment_fraction'] * (1 - df['emi_increase_fraction'])
    df['total_savings'] = (df['loan_amount'] * df['interest_rate'] / 100 / 12 * df['tenure_months'] -
                           calculate_emi(df['loan_amount'] * (1 - df['principal_repayment_fraction']),
                                         df['interest_rate'],
                                         df['tenure_months'])) * df['tenure_months']
    
    return df

# Train the machine learning model
def train_model(data):
    X = data[['loan_amount', 'interest_rate', 'tenure_months', 'monthly_investment', 'lump_sum', 'emi_increase_fraction', 'principal_repayment_fraction']]
    y = data['total_savings']
    
    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Create a pipeline
    pipeline = Pipeline([
        ('scaler', StandardScaler()),
        ('model', GradientBoostingRegressor())
    ])
    
    # Fit the model
    pipeline.fit(X_train, y_train)
    
    # Save the model
    joblib.dump(pipeline, 'savings_model.pkl')
    
    return pipeline

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

