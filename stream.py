import streamlit as st
import requests

st.set_page_config(page_title = "Loan Default Predictor")

st.title("🛖Loan Approval Predictor")

API = "http://127.0.0.1:8000/predict"

person_age = st.number_input("Person Age",18,100,30)
person_income= st.number_input("Person Income",1000,1000000,300000)
person_emp_length = st.number_input("Employment Length",0,120)
loan_amnt = st.number_input("Loan Ammount",1000,50000)
loan_percent_income = st.number_input("Loan % Income",0.0,1.0)
loan_int_rate = st.number_input("Lona Interest Rate",0.0,40.0)
cb_person_cred_hist_length = st.number_input("Credit History Lenght",0,50,8)

person_home_ownership = st.selectbox(
    "Home Ownership",['RENT', 'OWN', 'MORTGAGE', 'OTHER']
    )

loan_intent = st.selectbox(
    "Loan Intent", [
'EDUCATION', 'MEDICAL', 'PERSONAL', 'VENTURE', 'DEBTCONSOLIDATION','HOMEIMPROVEMENT']
)

loan_grade = st.selectbox(
    'Loan Grade',['B', 'C', 'A', 'D', 'E', 'F', 'G']
)

cb_person_default_on_file = st.selectbox("Default On File",["Y","N"])

if st.button("Predict"):
    payload  = {
        'person_age' : person_age,
        'person_income' : person_income,
        'person_home_ownership':person_home_ownership,
        'person_emp_length': person_emp_length,
        'loan_intent':loan_intent,
        'loan_grade':loan_grade,
        'loan_amnt':loan_amnt,
        'loan_int_rate':loan_int_rate,
        'loan_percent_income':loan_percent_income,
        'cb_person_default_on_file':cb_person_default_on_file,
        'cb_person_cred_hist_length': cb_person_cred_hist_length

    }

    response = requests.post(API,json=payload)

    if response.status_code == 200:
        result = response.json()
        st.success(f"Default Probability: {result['loan_default_probability']:.2f}")
        st.info(f"Predicted Status : {result['loan_status']}")
    else:
        st.error("Prediction Failed")
        