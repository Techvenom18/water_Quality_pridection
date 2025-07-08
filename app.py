import numpy as np 
import pandas as pd
import joblib 
import streamlit as st

# Load the model and structure
model = joblib.load("D:/WaterQualityPrediction-Project/pollution_model.pkl")
model_cols = joblib.load("D:\WaterQualityPrediction-Project\model_columns .pkl")

# Let's create a User interface
st.title("Water Pollutants Predictor")
st.write("Predict the water pollutants based on Year and Station ID")

# User inputs
year_input = st.number_input("Enter Year", min_value=2000, max_value=2100, value=2022)
Station_id = st.text_input("Enter Station ID", value='1')

# Predict button
if st.button('Predict'):
    if not Station_id:
        st.warning('Please enter the Station ID')
    else:
        # Prepare the input DataFrame
        input_df = pd.DataFrame({'year': [year_input], 'id': [Station_id]})
        input_encoded = pd.get_dummies(input_df, columns=['id'])

        # Align columns with model
        for col in model_cols:
            if col not in input_encoded.columns:
                input_encoded[col] = 0
        input_encoded = input_encoded[model_cols]

        # Predict
        predicted_pollutants = model.predict(input_encoded)[0]
        pollutants = ['O2', 'NO3', 'NO2', 'SO4', 'PO4', 'CL']

        # Display Results
        st.subheader(f"Predicted pollutant levels for the station '{Station_id}' in {year_input}:")
        for p, val in zip(pollutants, predicted_pollutants):
            st.write(f'{p}: {val:.2f}')



