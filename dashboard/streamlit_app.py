import streamlit as st
import requests

st.set_page_config(page_title="Churn Predictor", layout="centered")
st.title("📊 Customer Churn Prediction Dashboard")

st.markdown("Fill the details and click 'Predict Churn' to get the prediction from the Flask API.")

# Basic numerical/categorical inputs
SeniorCitizen = st.selectbox("Is the customer a senior citizen?", ["No", "Yes"])
Partner = st.selectbox("Has partner?", ["No", "Yes"])
Dependents = st.selectbox("Has dependents?", ["No", "Yes"])
tenure = st.slider("Tenure (months)", 0, 72, 12)
PhoneService = st.selectbox("Has phone service?", ["No", "Yes"])
PaperlessBilling = st.selectbox("Paperless billing?", ["No", "Yes"])
MonthlyCharges = st.number_input("Monthly Charges", 0.0, 200.0, 70.0)
TotalCharges = st.number_input("Total Charges", 0.0, 10000.0, 1500.0)
ServiceCount = st.slider("Total services subscribed", 0, 8, 4)

# One-hot encoded fields (keep all features model saw)
gender_Male = st.checkbox("Gender: Male")
MultipleLines_1 = st.checkbox("Multiple Lines: Yes")
MultipleLines_NoPhone = st.checkbox("Multiple Lines: No phone service")

InternetService_DSL = st.checkbox("Internet: DSL")
InternetService_Fiber = st.checkbox("Internet: Fiber Optic")

OnlineSecurity_1 = st.checkbox("Online Security: Yes")
OnlineSecurity_NoInternet = st.checkbox("Online Security: No internet service")

OnlineBackup_1 = st.checkbox("Online Backup: Yes")
OnlineBackup_NoInternet = st.checkbox("Online Backup: No internet service")

DeviceProtection_1 = st.checkbox("Device Protection: Yes")
DeviceProtection_NoInternet = st.checkbox("Device Protection: No internet service")

TechSupport_1 = st.checkbox("Tech Support: Yes")
TechSupport_NoInternet = st.checkbox("Tech Support: No internet service")

StreamingTV_1 = st.checkbox("Streaming TV: Yes")
StreamingTV_NoInternet = st.checkbox("Streaming TV: No internet service")

StreamingMovies_1 = st.checkbox("Streaming Movies: Yes")
StreamingMovies_NoInternet = st.checkbox("Streaming Movies: No internet service")

Contract_OneYear = st.checkbox("Contract: One year")
Contract_TwoYear = st.checkbox("Contract: Two year")

Payment_CreditCard = st.checkbox("Payment: Credit card (automatic)")
Payment_Electronic = st.checkbox("Payment: Electronic check")
Payment_Mailed = st.checkbox("Payment: Mailed check")

Tenure_1_2 = st.checkbox("Tenure Group: 1–2 years")
Tenure_2_4 = st.checkbox("Tenure Group: 2–4 years")
Tenure_4_5 = st.checkbox("Tenure Group: 4–5 years")
Tenure_5plus = st.checkbox("Tenure Group: 5+ years")

Monthly_Low = st.checkbox("Monthly Charges Bucket: Low")
Monthly_Med = st.checkbox("Monthly Charges Bucket: Medium")

if st.button("Predict Churn"):
    url = "https://0e2941f5-580a-473c-9e26-84a52e6e2c8d-00-oyz5z4wmdvwg.sisko.replit.dev/predict"

    payload = {
        "SeniorCitizen": 1 if SeniorCitizen == "Yes" else 0,
        "Partner": 1 if Partner == "Yes" else 0,
        "Dependents": 1 if Dependents == "Yes" else 0,
        "tenure": tenure,
        "PhoneService": 1 if PhoneService == "Yes" else 0,
        "PaperlessBilling": 1 if PaperlessBilling == "Yes" else 0,
        "MonthlyCharges": MonthlyCharges,
        "TotalCharges": TotalCharges,
        "ServiceCount": ServiceCount,
        "gender_Male": gender_Male,
        "MultipleLines_1": MultipleLines_1,
        "MultipleLines_No phone service": MultipleLines_NoPhone,
        "InternetService_DSL": InternetService_DSL,
        "InternetService_Fiber optic": InternetService_Fiber,
        "OnlineSecurity_1": OnlineSecurity_1,
        "OnlineSecurity_No internet service": OnlineSecurity_NoInternet,
        "OnlineBackup_1": OnlineBackup_1,
        "OnlineBackup_No internet service": OnlineBackup_NoInternet,
        "DeviceProtection_1": DeviceProtection_1,
        "DeviceProtection_No internet service": DeviceProtection_NoInternet,
        "TechSupport_1": TechSupport_1,
        "TechSupport_No internet service": TechSupport_NoInternet,
        "StreamingTV_1": StreamingTV_1,
        "StreamingTV_No internet service": StreamingTV_NoInternet,
        "StreamingMovies_1": StreamingMovies_1,
        "StreamingMovies_No internet service": StreamingMovies_NoInternet,
        "Contract_One year": Contract_OneYear,
        "Contract_Two year": Contract_TwoYear,
        "PaymentMethod_Credit card (automatic)": Payment_CreditCard,
        "PaymentMethod_Electronic check": Payment_Electronic,
        "PaymentMethod_Mailed check": Payment_Mailed,
        "TenureGroup_1–2 years": Tenure_1_2,
        "TenureGroup_2–4 years": Tenure_2_4,
        "TenureGroup_4–5 years": Tenure_4_5,
        "TenureGroup_5+ years": Tenure_5plus,
        "MonthlyChargesBucket_Low": Monthly_Low,
        "MonthlyChargesBucket_Medium": Monthly_Med
    }

    try:
        res = requests.post(url, json=payload)
        result = res.json()

        if "error" in result:
            st.error(f"❌ API Error: {result['error']}")
        else:
            st.success(f"🎯 Churn Prediction: {result['Churn']}")
            st.metric("📈 Probability", f"{result['Churn_Probability'] * 100:.2f}%")

    except Exception as e:
        st.error(f"🚨 Request failed: {e}")





