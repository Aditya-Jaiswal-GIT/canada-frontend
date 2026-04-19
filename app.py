import streamlit as st
import requests
from URL import url
# FastAPI endpoint
API_URL = url

st.set_page_config(page_title="Per Capita Income Predictor", layout="centered")

st.title("📊 Canada Per Capita Income Predictor")
st.markdown("Enter a year (1000 - 9999) to predict per capita income.")

# Input
year = st.number_input("Enter Year", min_value=1000, max_value=9999, value=2020)

# Button
if st.button("Predict"):
    try:
        response = requests.post(API_URL, params={"x": int(year)})

        if response.status_code == 200:
            data = response.json()
            
            # Extract value dynamically
            prediction = list(data.values())[0]

            st.success(f"💰 Predicted Per Capita Income: {prediction} US$")
        else:
            st.error(f"❌ Error: {response.json()}")

    except requests.exceptions.ConnectionError:
        st.error("⚠️ Could not connect to FastAPI server. Make sure it's running.")