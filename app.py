import streamlit as st
from text_utils import text_cleaner_func, apply_text_cleaner

import pickle
import pandas as pd


answer = {
    "Data Science": 6,
    "HR	": 12,
    "Advocate": 0,
    "Arts": 1,
    "Web Designing": 24,
    "Mechanical Engineer": 16,
    "Sales": 22,
    "Health and fitness": 14,
    "Civil Engineer": 5,
    "Java Developer": 15,
    "Business Analyst": 4,
    "SAP Developer": 21,
    "Automation Testing": 2,
    "Electrical Engineering": 11,
    "Operations Manager": 18,
    "Python Developer": 20,
    "DevOps Engineer": 8,
    "Network Security Engineer": 17,
    "PMO": 19,
    "Database": 7,
    "Hadoop	": 13,
    "ETL Developer": 10,
    "DotNet Developer": 9,
    "Blockchain": 3,
    "Testing": 23,
}


model_path = "DTCModel.pkl"

st.title("Resume Skill Check")
message_input = st.text_area("Enter your message here:")

if st.button("Predict"):
    if len(message_input.strip()) <= 1:
        st.error("Enter a valid message.")
    else:
        with open(model_path, "rb") as model_file:
            model = pickle.load(model_file)

        prediction = model.predict(pd.Series([message_input]))[0]
        if prediction in answer.values():
            category = list(answer.keys())[list(answer.values()).index(prediction)]
            st.success(f"Prediction: {category}")
