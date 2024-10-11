import streamlit as st
import numpy as np

# Title and Introduction
st.title("Loan & Investment Optimization Platform")
st.subheader("Maximize your wealth by optimizing your loan payments and investments.")

# Sidebar Navigation for Different Features
st.sidebar.title("Menu")
page = st.sidebar.selectbox("Choose a feature", ["Home", "Loan Optimization", "Investment Options", "Financial Insights", "Contact Us"])

# Home Page
if page == "Home":
    st.write("""
        Welcome to the Loan & Investment Optimization Platform! 
        Here, you can manage your loans and explore investment strategies to maximize your wealth.
    """)
    st.image("https://via.placeholder.com/500x300", caption="Maximize Your Wealth")

# Loan Optimization Page
if page == "Loan Optimization":
    st.header("Loan Optimization")
    
    # Input Fields for Loan Details
    loan_amount = st.number_input("Enter your loan amount (in USD):", min_value=1000, step=500)
    interest_rate = st.number_input("Current interest rate (%):", min_value=1.0, max_value=20.0, step=0.1)
    emi = st.number_input("Your current EMI (in USD):", min_value=100, step=50)
    tenure_years = st.number_input("Loan tenure (years):", min_value=1, max_value=30)
    
    # Calculate Options
    if st.button("Calculate Loan Options"):
        principal_payment = 0.10 * loan_amount  # Example logic
        reduced_emi = emi * 0.9
        st.write(f"By paying 10% towards the principal, your EMI can reduce to: **${reduced_emi:.2f}**")
        st.write(f"You can also make a lump-sum payment of **${principal_payment:.2f}** towards the principal.")
    
    # Additional Loan Strategy
    st.subheader("Loan Repayment Strategy")
    strategy = st.radio("Choose your repayment strategy:", ["Increase EMI", "Lump Sum Payment", "Refinance"])
    if strategy == "Increase EMI":
        st.write("Increasing EMI helps in reducing the loan tenure.")
    elif strategy == "Lump Sum Payment":
        st.write("Lump sum payments towards the principal reduce the loan faster.")
    else:
        st.write("Refinancing at a lower rate can save you on interest costs.")

# Investment Options Page
if page == "Investment Options":
    st.header("Investment Opportunities")
    
    # Input Fields for Investment Preferences
    risk_level = st.selectbox("Select your risk tolerance level:", ["Low", "Medium", "High"])
    amount_invest = st.number_input("Amount to invest (in USD):", min_value=500, step=100)
    duration = st.number_input("Investment duration (years):", min_value=1, max_value=30)
    
    # Show Investment Plans
    if st.button("Show Investment Plans"):
        if risk_level == "Low":
            st.write("Recommended Investment: **Government Bonds** - Safe but lower returns.")
        elif risk_level == "Medium":
            st.write("Recommended Investment: **Mutual Funds** - Balanced risk and returns.")
        else:
            st.write("Recommended Investment: **Stocks** - Higher risk but potentially higher returns.")
    
    st.write("Customize your investment strategy to balance your loans and wealth growth.")

# Financial Insights Page
if page == "Financial Insights":
    st.header("Financial Insights")
    
    # Provide insights based on user data (placeholder for future ML model predictions)
    st.write("Here are some insights based on your financial data:")
    st.write("""
        - Paying off 20% of your loan early can save you $5,000 in interest.
        - Based on your risk profile, a 5-year investment in mutual funds could yield 8-12% returns.
    """)
    
    # Add visualizations (optional)
    st.subheader("Loan vs. Investment Comparison")
    st.line_chart(np.random.randn(10, 2))  # Placeholder chart for comparison (replace with actual data)

# Contact Us Page
if page == "Contact Us":
    st.header("Contact Us")
    st.write("Have any questions? Feel free to reach out to us!")

    # Contact Form
    name = st.text_input("Your Name:")
    email = st.text_input("Your Email:")
    message = st.text_area("Your Message:")
    if st.button("Submit"):
        st.success(f"Thanks {name}! We will get back to you at {email} soon.")
