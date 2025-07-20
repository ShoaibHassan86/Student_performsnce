import streamlit as st
import pandas as pd
import pickle

# Load model
import os
model_path = os.path.join(os.path.dirname(__file__), 'performance_index.sav')
model = pickle.load(open(model_path, 'rb'))

# Page config
st.set_page_config(page_title="Student Performance Predictor", page_icon="📊", layout="centered")

# Title with style
st.markdown("<h1 style='text-align: center; color: navy;'>🎓 Student Performance Index Predictor</h1>", unsafe_allow_html=True)
st.markdown("---")

# Input fields
st.markdown("### 📝 Enter Student Details:")
col1, col2 = st.columns(2)

with col1:
    hours_studied = st.number_input("📘 Hours Studied", min_value=0.0, max_value=10.0, step=0.5)

    extracurricular = st.radio("🎭 Extracurricular Activities", ['Yes', 'No'], index=0)

    sleep_hours = st.number_input("💤 Average Sleep Hours", min_value=0.0, max_value=10.0, step=0.5)

with col2:
    previous_scores = st.number_input("📊 Previous Scores (out of 100)", min_value=0.0, max_value=100.0, step=1.0)

    sample_papers = st.slider("📄 Sample Papers Practiced", min_value=0, max_value=10, value=3)

# Predict Button
st.markdown("---")
if st.button("🔍 Predict Performance Index"):
    extracurricular_encoded = 1 if extracurricular == 'Yes' else 0

    # Create input DataFrame
    input_df = pd.DataFrame({
        'Hours Studied': [hours_studied],
        'Previous Scores': [previous_scores],
        'Extracurricular Activities': [extracurricular_encoded],
        'Sleep Hours': [sleep_hours],
        'Sample Question Papers Practiced': [sample_papers]
    })

    # Prediction
    prediction = model.predict(input_df)[0]

    # Display result
    st.success(f"🎯 **Expected Performance Index**: `{prediction:.2f}`")
    st.balloons()
