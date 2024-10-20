import streamlit as st
import numpy as np
from PIL import Image


# Set custom CSS styles for fancy fonts and backgrounds
st.markdown("""
    <style>
    body {
        background-color: #f5f5f5;
    }
    .main {
        background-color: #ffffff;
        font-family: 'Arial', sans-serif;
    }
    h1 {
        font-size: 40px;
        color: #336699;
    }
    .sidebar .sidebar-content {
        background-color: #336699;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# Title and Introduction
st.title("💸 Loan & Investment Optimization Platform")
st.write("Maximize your wealth by optimizing your loan payments and investments.")

# Sidebar with navigation and a header image
st.sidebar.image("image.jpeg", caption="Optimize Your Wealth", use_column_width=True)
st.sidebar.title("📊 Menu")
page = st.sidebar.selectbox("Choose a feature", ["Home", "Loan Optimization", "Investment Options", "Current Rates", "Market Analysis", "Contact Us"])

# Home Page
if page == "Home":
    st.header("Welcome to the Loan & Investment Optimization Platform!")
    st.write("Manage your loans, explore investment opportunities, and grow your wealth.")
    st.image("https://img.freepik.com/free-vector/finance-financial-performance-concept-illustration_53876-40450.jpg", caption="Maximize Your Wealth", use_column_width=True)

# Loan Optimization Page
if page == "Loan Optimization":
    st.header("💰 Loan Optimization")

    # Input Fields for Loan Details
    loan_amount = st.number_input("Enter your loan amount (in USD):", min_value=1000, step=500)
    interest_rate = st.number_input("Current interest rate (%):", min_value=1.0, max_value=20.0, step=0.1)
    emi = st.number_input("Your current EMI (in USD):", min_value=100, step=50)
    tenure_years = st.number_input("Loan tenure (years):", min_value=1, max_value=30)

    # Fancy Calculate Options Button
    if st.button("🔍 Calculate Best Loan Options"):
        principal_payment = 0.10 * loan_amount
        reduced_emi = emi * 0.9
        st.success(f"By paying 10% towards the principal, your EMI can reduce to: **${reduced_emi:.2f}**")
        st.info(f"You can make a lump-sum payment of **${principal_payment:.2f}** towards the principal to save interest.")

    # Additional Loan Strategy with Progress Bar
    st.subheader("Loan Repayment Strategy")
    strategy = st.radio("Choose your repayment strategy:", ["Increase EMI", "Lump Sum Payment", "Refinance"])
    if strategy == "Increase EMI":
        st.write("Increasing EMI can reduce the loan tenure.")
        st.progress(0.5)
    elif strategy == "Lump Sum Payment":
        st.write("Lump sum payments towards the principal reduce the loan faster.")
        st.progress(0.8)
    else:
        st.write("Refinancing at a lower rate can save you interest.")
        st.progress(0.3)

# Investment Options Page
if page == "Investment Options":
    st.header("💹 Investment Opportunities")

    # Input Fields for Investment Preferences
    risk_level = st.selectbox("Select your risk tolerance level:", ["Low", "Medium", "High"])
    amount_invest = st.number_input("Amount to invest (in USD):", min_value=500, step=100)
    duration = st.number_input("Investment duration (years):", min_value=1, max_value=30)

    # Show Investment Plans
    if st.button("📊 Show Investment Plans"):
        if risk_level == "Low":
            st.write("Recommended: **Government Bonds** (Low Risk)")
        elif risk_level == "Medium":
            st.write("Recommended: **Mutual Funds** (Medium Risk)")
        else:
            st.write("Recommended: **Stocks** (High Risk)")

    # Additional info
    st.write("🔍 Customize your investment to maximize returns!")

# Current Rates Page
if page == "Current Rates":
    st.header("📉 Current Interest & Loan Rates")
    st.write("Keep track of current loan and investment rates for better decisions.")

    # Table showing dummy data (could be scraped dynamically)
    st.table({
        "Loan Type": ["Home Loan", "Car Loan", "Personal Loan"],
        "Interest Rate": ["7.5%", "8.2%", "11.5%"]
    })

# Market Analysis Page
if page == "Market Analysis":
    st.header("📈 Market Analysis")
    st.write("Get insights on the latest market trends.")

    # Placeholder chart for market analysis
    st.line_chart(np.random.randn(10, 2))

    st.write("🔍 Analyze market trends and compare your investment strategies with the latest data.")

# Contact Us Page
if page == "Contact Us":
    st.header("📞 Contact Us")
    st.write("Have any questions? Reach out to us!")

    # Contact Form
    name = st.text_input("Your Name:")
    email = st.text_input("Your Email:")
    message = st.text_area("Your Message:")
    if st.button("✉️ Submit"):
        st.success(f"Thanks {name}! We will get back to you at {email} soon.")
