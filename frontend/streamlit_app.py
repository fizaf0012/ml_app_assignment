import streamlit as st
import requests
import os

st.set_page_config(page_title="Booking Cancellation Predictor")

# Configurable API URL
API_URL = os.getenv("API_URL", "http://localhost:8000/predict")

st.title("Hotel Booking Cancellation Predictor")

with st.form("prediction_form"):
    st.subheader("Enter Booking Details")
    
    col1, col2 = st.columns(2)
    with col1:
        lead_time = st.number_input("Lead Time (days)", min_value=0, value=50)
        adults = st.number_input("Number of Adults", min_value=1, value=2)
    with col2:
        children = st.number_input("Number of Children", min_value=0, value=0)
        changes = st.number_input("Booking Changes Made", min_value=0, value=0)
    
    parking = st.number_input("Car Parking Spaces Needed", min_value=0, value=0)
    
    submitted = st.form_submit_button("Predict Cancellation Risk")
    
    if submitted:
        data = {
            "lead_time": lead_time,
            "adults": adults,
            "children": children,
            "booking_changes": changes,
            "required_car_parking_spaces": parking
        }
        
        try:
            response = requests.post(API_URL, json=data)
            if response.status_code == 200:
                result = response.json()
                prob = result["cancellation_probability"] * 100
                
                st.metric("Cancellation Probability", f"{prob:.1f}%")
                if result["will_cancel"]:
                    st.error("High Risk of Cancellation")
                else:
                    st.success("Low Risk of Cancellation")
            else:
                st.error(f"API Error: {response.text}")
        except Exception as e:
            st.error(f"Connection failed: {str(e)}")