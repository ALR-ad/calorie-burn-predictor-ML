import streamlit as st
import pickle
import numpy as np

# Load model & scaler
model = pickle.load(open('model.pkl', 'rb'))
sc = pickle.load(open('scaler.pkl', 'rb'))

st.title(" Calories Burn Predictor")

# ---- INPUTS ----
age = st.number_input("Age")
weight = st.number_input("Weight (kg)")
height = st.number_input("Height (m)")
max_bpm = st.number_input("Max BPM")
avg_bpm = st.number_input("Avg BPM")
rest_bpm = st.number_input("Resting BPM")
duration = st.number_input("Session Duration (hours)")
fat = st.number_input("Fat Percentage")
water = st.number_input("Water Intake (liters)")
freq = st.number_input("Workout Frequency (days/week)")
exp = st.selectbox("Experience Level", ["Beginner", "Intermediate", "Advanced"])
bmi = st.number_input("BMI")

gender = st.selectbox("Gender", ["Male", "Female"])
workout = st.selectbox("Workout Type", ["Cardio", "HIIT", "Strength", "Yoga"])

# ---- ENCODING ----

# Experience Level
exp_map = {"Beginner": 0, "Intermediate": 1, "Advanced": 2}
exp = exp_map[exp]

# Gender (IMPORTANT: only Gender_Male exists)
gender_male = 1 if gender == "Male" else 0

# Workout Type (drop_first=True was used)
workout_hiit = 1 if workout == "HIIT" else 0
workout_strength = 1 if workout == "Strength" else 0
workout_yoga = 1 if workout == "Yoga" else 0
# Cardio = all zeros


input_data = np.array([[
    age,
    weight,
    height,
    max_bpm,
    avg_bpm,
    rest_bpm,
    duration,
    fat,
    water,
    freq,
    exp,
    bmi,
    gender_male,
    workout_hiit,
    workout_strength,
    workout_yoga
]])

# ---- PREDICT ----
if st.button("Predict"):
    input_scaled = sc.transform(input_data)
    prediction = model.predict(input_scaled)

    st.success(f"🔥 Calories Burned: {prediction[0]:.2f}")