import streamlit as st
import pandas as pd
import os
import joblib

# =========================
# LOAD MODEL & FEATURE
# =========================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model_path = os.path.join(BASE_DIR, 'model_rf.pkl')
feature_path = os.path.join(BASE_DIR, 'feature_columns.pkl')

model = joblib.load(model_path)
feature_columns = joblib.load(feature_path)

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="Student Dropout Prediction",
    layout="centered"
)

st.title("🎓 Student Dropout Prediction")
st.write(
    "Prototype machine learning untuk memprediksi "
    "risiko mahasiswa melakukan dropout."
)

# =========================
# INPUT USER
# =========================
st.subheader("Input Student Data")

age = st.number_input(
    "Age at Enrollment",
    min_value=15,
    max_value=70,
    value=20
)

admission_grade = st.number_input(
    "Admission Grade",
    min_value=0.0,
    max_value=200.0,
    value=120.0
)

previous_qualification_grade = st.number_input(
    "Previous Qualification Grade",
    min_value=0.0,
    max_value=200.0,
    value=120.0
)

sem1_approved = st.number_input(
    "1st Semester Approved Units",
    min_value=0,
    max_value=20,
    value=5
)

sem2_approved = st.number_input(
    "2nd Semester Approved Units",
    min_value=0,
    max_value=20,
    value=5
)

sem1_grade = st.number_input(
    "1st Semester Grade",
    min_value=0.0,
    max_value=20.0,
    value=10.0
)

sem2_grade = st.number_input(
    "2nd Semester Grade",
    min_value=0.0,
    max_value=20.0,
    value=10.0
)

sem1_evaluations = st.number_input(
    "1st Semester Evaluations",
    min_value=0,
    max_value=40,
    value=6
)

sem2_evaluations = st.number_input(
    "2nd Semester Evaluations",
    min_value=0,
    max_value=40,
    value=6
)

gender = st.selectbox(
    "Gender",
    ["Female", "Male"]
)

debtor = st.selectbox(
    "Debtor",
    ["No", "Yes"]
)

tuition = st.selectbox(
    "Tuition Fees Up To Date",
    ["Yes", "No"]
)

# =========================
# PREDICTION
# =========================
if st.button("Predict"):

    # ---------------------
    # INPUT DATAFRAME
    # ---------------------
    input_data = pd.DataFrame({
        'Age_at_enrollment': [age],
        'Admission_grade': [admission_grade],
        'Previous_qualification_grade': [previous_qualification_grade],
        'Curricular_units_1st_sem_approved': [sem1_approved],
        'Curricular_units_2nd_sem_approved': [sem2_approved],
        'Curricular_units_1st_sem_grade': [sem1_grade],
        'Curricular_units_2nd_sem_grade': [sem2_grade],
        'Curricular_units_1st_sem_evaluations': [sem1_evaluations],
        'Curricular_units_2nd_sem_evaluations': [sem2_evaluations],

        # one-hot encoded columns
        'Gender_1': [1 if gender == "Male" else 0],
        'Debtor_1': [1 if debtor == "Yes" else 0],
        'Tuition_fees_up_to_date_1': [1 if tuition == "Yes" else 0]
    })

    # ---------------------
    # SAMAKAN KOLOM
    # ---------------------
    input_data = input_data.reindex(
        columns=feature_columns,
        fill_value=0
    )

    # ---------------------
    # PREDICT
    # ---------------------
    prediction = model.predict(input_data)[0]

    probability = model.predict_proba(input_data)[0][1]

    # =====================
    # OUTPUT
    # =====================
    st.subheader("Prediction Result")

    if prediction == 1:
        st.error("⚠️ High Risk of Dropout")
    else:
        st.success("✅ Low Risk of Dropout")

    st.write(f"Dropout Probability: **{probability:.2%}**")