
import streamlit as st
# Title: Personal Health Profile
import os
from backend.heath_llm import predict_health

def request_diabetes(age, gender, height, weight, drinking, smoking, alcohol, glucose, blood_pressure_h, blood_pressure_l):
  bmi=weight/(height**2)
  bmi=round(bmi,2)
  hypertension=0
  if(blood_pressure_h>130):
    hypertension=1
  diabetes_endpoint="2830191308407046144"
  diabetes_instance={
   "gender" : gender,
   "age" : age,
   "smoking" : smoking,
   "bmi": bmi,
   "blood_glucose_level": glucose,
   "hypertension": hypertension,
   "heart_disease": 0
  }
  health_response = predict_health(project= "rick-vertex-ai", endpoint=diabetes_endpoint, instance=diabetes_instance)
  st.write(health_response)



st.set_page_config(layout="wide")
st.title("Personal Health Profile")
# Create a form
with st.form("Health Profile Form"):

# Prompt for enter profile information
  age = st.number_input("Age")
  gender = st.selectbox("Gender", ["male", "female"])
  height = st.number_input("Height (cm)")
  weight = st.number_input("Weight (kg)")
  drinking = st.selectbox("Drinking", ["yes", "no"])
  smoking = st.selectbox("Smoking", ["yes", "no"])
  alcohol = st.selectbox("Alcohol", ["yes", "no"])
  glucose = st.number_input("Glucose (mg/dL)")
  blood_pressure_h = st.number_input("Blood Pressure (H)")
  blood_pressure_l = st.number_input("Blood Pressure (L)")
  submitted = st.form_submit_button("Save")
  if submitted:
       request_diabetes(age, gender, height, weight, drinking, smoking, alcohol, glucose, blood_pressure_h, blood_pressure_l)


