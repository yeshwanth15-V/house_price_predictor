import streamlit as st
import pickle
import numpy as np

# -------------------------
# Page Configuration
# -------------------------
st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏠",
    layout="centered"
)

# -------------------------
# Load Trained Model
# -------------------------
with open("model_pickle", "rb") as file:
    model = pickle.load(file)

# -------------------------
# Title
# -------------------------
st.title("🏠 House Price Prediction")
st.write("Enter the house details below to predict the estimated price.")

st.divider()

# -------------------------
# User Inputs
# -------------------------
area = st.number_input(
    "Area (Square Feet)",
    min_value=100,
    max_value=10000,
    value=1414
)

bathroom = st.number_input(
    "Number of Bathrooms",
    min_value=1,
    max_value=10,
    value=2
)

bedroom = st.number_input(
    "Number of Bedrooms",
    min_value=1,
    max_value=10,
    value=3
)

# -------------------------
# Prediction
# -------------------------
if st.button("Predict House Price"):

    input_data = np.array([[area, bathroom, bedroom]])

    prediction = model.predict(input_data)

    st.success(f"🏡 Estimated House Price: ₹ {prediction[0]:,.2f}")
