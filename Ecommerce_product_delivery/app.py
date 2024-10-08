import pandas as pd
import pickle
import streamlit as st

# Load model
model_path = r'RF_model.pkl'
with open(model_path, 'rb') as f:
    model = pickle.load(f)

# Create Streamlit app
st.title("E-Commerce Product Delivery Prediction")

# Input fields for features
warehouse_block = st.selectbox("Warehouse Block", ["A", "B", "C", "D", "E"])
customer_care_calls = st.number_input("Customer Care Calls", min_value=0, max_value=10, value=4)
customer_rating = st.slider("Customer Rating", min_value=1, max_value=5, value=2)
cost_of_the_product = st.number_input("Cost of the Product", min_value=1, max_value=10000, value=400)
prior_purchases = st.number_input("Number of Prior Purchases", min_value=0, max_value=100, value=3)
discount_offered = st.number_input("Discount Offered (%)", min_value=0, max_value=100, value=11)
weight_in_gms = st.number_input("Weight of the Product (in grams)", min_value=1, max_value=10000, value=600)

# Encoding categorical features
warehouse_mapping = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4}
warehouse_encoded = warehouse_mapping[warehouse_block]

# Create input data
input_data = pd.DataFrame({
    'Warehouse_block': [warehouse_encoded],
    'Customer_care_calls': [customer_care_calls],
    'Customer_rating': [customer_rating],
    'Cost_of_the_Product': [cost_of_the_product],
    'Prior_purchases': [prior_purchases],
    'Discount_offered': [discount_offered],
    'Weight_in_gms': [weight_in_gms]
})

# Predict
if st.button("Predict"):
    prediction = model.predict(input_data)[0]
    if prediction == 1:
        st.success(" ON TIME DELIVERY")
    else:
        st.warning("LATE DELIVERY")
