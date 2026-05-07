import joblib
import pandas as pd

# Load model

model = joblib.load("model.pkl")
preprocessor = joblib.load("preprocessor.pkl")

def predict(input_data):
    """
    input data = dictonary (paling aman)
    """

    df = pd.DataFrame([input_data])

    # preprocessing
    transformed = preprocessor.transform(df)

    # prediction
    prob = model.predict_proba(transformed)[0][1]

    return{
        "attrition_probability": float(prob),
        "prediction": int(prob > 0.5)
    }

if __name__ == "__main__":
    sample_input = {
        'Age': 40,
        'BusinessTravel': 'Travel_Rarely',
        'DailyRate': 1141,
        'Department': 'Research & Development',
        'DistanceFromHome': 11,
        'Education': 2,
        'EducationField': 'Medical',
        'EnvironmentSatisfaction': 1,
        'Gender': 'Female',
        'HourlyRate': 61,
        'JobInvolvement': 1,
        'JobLevel': 2,
        'JobRole': 'Healthcare Representative',
        'JobSatisfaction': 2,
        'MaritalStatus': 'Married',
        'MonthlyIncome': 4777,
        'MonthlyRate': 14382,
        'NumCompaniesWorked': 5,
        'OverTime': 'Yes',
        'PercentSalaryHike': 15,
        'PerformanceRating': 3,
        'RelationshipSatisfaction': 1,
        'StockOptionLevel': 0,
        'TotalWorkingYears': 15,
        'TrainingTimesLastYear': 2,
        'WorkLifeBalance': 1,
        'YearsAtCompany': 1,
        'YearsInCurrentRole': 0,
        'YearsSinceLastPromotion': 0,
        'YearsWithCurrManager': 0
    }

    result = predict(sample_input)
    print(result)