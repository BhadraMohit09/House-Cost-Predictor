import streamlit as st
import pandas as pd
import pickle

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

st.title('House Cost Predictor(INR)')

st.write("Enter the features of the house to predict the price:")

area = st.number_input('Area (sq. ft)', min_value=500, max_value=10000, step=10)
bedrooms = st.number_input('Number of Bedrooms', min_value=1, max_value=10, step=1)
bathrooms = st.number_input('Number of Bathrooms', min_value=1, max_value=10, step=1)
rooms = st.number_input('Total number of Rooms', min_value=1, max_value=20, step=1)

input_data = pd.DataFrame({'area': [area], 'bedrooms': [bedrooms], 'bathrooms': [bathrooms], 'rooms': [rooms]})

usd_to_inr = 83.0

if st.button('Predict'):
    prediction = model.predict(input_data)
    
    
    price_in_inr = prediction[0] * usd_to_inr
    
    st.write(f"The predicted cost of house is:: ₹{price_in_inr:,.2f}")
