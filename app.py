import streamlit as st
import numpy as np
import pickle

# Load model
model = pickle.load(open("car_price_model.pkl", "rb"))

st.title("🚗 Car Price Prediction App")

# Inputs (example)
year = st.number_input("Year", 2000, 2025)
km_driven = st.number_input("KM Driven", 0, 200000)
fuel = st.selectbox("Fuel Type", ["Petrol", "Diesel"])

# Convert categorical to numeric (example)
fuel_map = {"Petrol": 0, "Diesel": 1}
fuel = fuel_map[fuel]

# Prediction
if st.button("Predict Price"):
    features = np.array([[year, km_driven, fuel]])
    prediction = model.predict(features)
    st.success(f"Estimated Price: ₹{prediction[0]:,.2f}")