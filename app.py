import streamlit as st
import pickle
import numpy as np

# Page Configuration
st.set_page_config(
    page_title="Prediction App",
    page_icon="📊",
    layout="centered"
)

# Load Model
with open("model_pickle", "rb") as file:
    model = pickle.load(file)

# Title
st.title("📊 Machine Learning Prediction App")
st.write("Enter the values below to get the prediction.")

st.divider()

# Input Fields
feature1 = st.number_input("Feature 1", value=0.0)
feature2 = st.number_input("Feature 2", value=0.0)
feature3 = st.number_input("Feature 3", value=0.0)

# Prediction
if st.button("Predict"):
    input_data = np.array([[feature1, feature2, feature3]])
    prediction = model.predict(input_data)

    st.success(f"Prediction: {prediction[0]:.2f}")
