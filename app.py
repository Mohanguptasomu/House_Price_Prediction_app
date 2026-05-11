# create environment : python -m venv myenv
# activate environment : myenv\Scripts\activate
# install libraries :
# pip install streamlit pandas numpy scikit-learn

# run :
# streamlit run app.py

import pickle
import pandas as pd
import numpy as np
import streamlit as st

# Load trained Linear Regression model
with open('model_lr.pkl', 'rb') as f:
    model = pickle.load(f)

# UI
st.title("🏠 House Price Prediction")

square_footage = st.number_input('Square Footage', 500, 15000, 2000)
num_bedrooms = st.number_input('Bedrooms', 1, 10, 3)
num_bathrooms = st.number_input('Bathrooms', 1, 10, 2)
year_built = st.number_input('Year Built', 1800, 2025, 2000)
lot_size = st.number_input('Lot Size', 0.0, 20.0, 0.5)
garage_size = st.number_input('Garage Size', 0, 5, 2)
neighborhood_quality = st.slider('Neighborhood Quality', 1, 10, 5)

if st.button("Predict Price"):

    input_data = pd.DataFrame({
        'Square_Footage': [square_footage],
        'Num_Bedrooms': [num_bedrooms],
        'Num_Bathrooms': [num_bathrooms],
        'Year_Built': [year_built],
        'Lot_Size': [lot_size],
        'Garage_Size': [garage_size],
        'Neighborhood_Quality': [neighborhood_quality]
    })

    # Prediction
    prediction = model.predict(input_data)

    # If trained using log1p()
    actual_price = np.expm1(prediction[0])

    st.success(f"Estimated House Price: ${actual_price:,.2f}")