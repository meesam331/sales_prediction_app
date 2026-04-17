import streamlit as st
import joblib
import pandas as pd
import numpy as np

# Set page config
st.set_page_config(
    page_title="Sales Forecasting App",
    page_icon="💰",
    layout="wide"
)

# Load model and scaler
@st.cache_resource
def load_model_and_scaler():
    model = joblib.load('sales_forecasting_model.pkl')
    scaler = joblib.load('sales_scaler.pkl')
    return model, scaler

model, scaler = load_model_and_scaler()

# App title and description
st.title("💰 Sales Forecasting Application")
st.markdown("---")
st.write("Enter the product details below to predict the sales amount using our trained Linear Regression model.")

# Create two columns layout
col1, col2 = st.columns(2)

# Input fields
with col1:
    st.subheader("📋 Product Information")
    
    price_each = st.number_input(
        "Price Each ($)",
        min_value=20.0,
        max_value=110.0,
        value=85.0,
        step=0.1,
        help="Price per unit (20-110)"
    )
    
    msrp = st.number_input(
        "MSRP ($)",
        min_value=30.0,
        max_value=220.0,
        value=100.0,
        step=1.0,
        help="Manufacturer's Suggested Retail Price (30-220)"
    )
    
    quantity_ordered = st.number_input(
        "Quantity Ordered",
        min_value=6,
        max_value=100,
        value=35,
        step=1,
        help="Number of units ordered (6-100)"
    )

with col2:
    st.subheader("📦 Order Details")
    
    order_number = st.number_input(
        "Order Number",
        min_value=10100,
        max_value=10430,
        value=10258,
        step=1,
        help="Order identification number (10100-10430)"
    )
    
    year_id = st.selectbox(
        "Year",
        options=[2003, 2004, 2005],
        help="Year of the order"
    )
    
    st.markdown("")  # Spacing

# Create prediction section
st.markdown("---")
st.subheader("🎯 Prediction")

# Prepare input data
input_data = pd.DataFrame({
    'PRICEEACH': [price_each],
    'MSRP': [msrp],
    'QUANTITYORDERED': [quantity_ordered],
    'ORDERNUMBER': [order_number],
    'YEAR_ID': [year_id]
})

# Scale the input
input_scaled = scaler.transform(input_data)

# Make prediction
prediction = model.predict(input_scaled)[0]

# Display prediction
col1, col2, col3 = st.columns([1, 1, 1])

with col2:
    st.metric(
        label="Predicted Sales Amount",
        value=f"${prediction:,.2f}",
        delta="Based on Linear Regression Model"
    )

# Display input summary
st.markdown("---")
st.subheader("📊 Input Summary")

summary_col1, summary_col2 = st.columns(2)

with summary_col1:
    st.write(f"**Price Each:** ${price_each:.2f}")
    st.write(f"**MSRP:** ${msrp:.2f}")
    st.write(f"**Quantity Ordered:** {quantity_ordered} units")

with summary_col2:
    st.write(f"**Order Number:** {order_number}")
    st.write(f"**Year:** {year_id}")

# Model information
st.markdown("---")
st.subheader("ℹ️ Model Information")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Training R² Score", "0.8072")

with col2:
    st.metric("Test R² Score", "0.7607")

with col3:
    st.metric("Test RMSE", "$1,021.98")

st.info(
    "✅ This model was trained on actual sales data using Linear Regression. "
    "It considers price, quantity, and other order details to forecast sales amounts."
)
