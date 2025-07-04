import requests

url = 'https://0e2941f5-580a-473c-9e26-84a52e6e2c8d-00-oyz5z4wmdvwg.sisko.replit.dev/predict'

data = {
    "SeniorCitizen": 0,
    "Partner": 1,
    "Dependents": 0,
    "tenure": 1,
    "PhoneService": 0,
    "PaperlessBilling": 1,
    "MonthlyCharges": 29.85,
    "TotalCharges": 29.85,
    "ServiceCount": 1,
    "gender_Male": 1,
    "MultipleLines_1": 0,
    "MultipleLines_No phone service": 1,
    "InternetService_DSL": 1,
    "InternetService_Fiber optic": 0,
    "OnlineSecurity_1": 0,
    "OnlineSecurity_No internet service": 0,
    "OnlineBackup_1": 1,
    "OnlineBackup_No internet service": 0,
    "DeviceProtection_1": 0,
    "DeviceProtection_No internet service": 0,
    "TechSupport_1": 0,
    "TechSupport_No internet service": 0,
    "StreamingTV_1": 0,
    "StreamingTV_No internet service": 0,
    "StreamingMovies_1": 0,
    "StreamingMovies_No internet service": 0,
    "Contract_One year": 0,
    "Contract_Two year": 0,
    "PaymentMethod_Credit card (automatic)": 0,
    "PaymentMethod_Electronic check": 1,
    "PaymentMethod_Mailed check": 0,
    "TenureGroup_1–2 years": 0,
    "TenureGroup_2–4 years": 0,
    "TenureGroup_4–5 years": 0,
    "TenureGroup_5+ years": 0,
    "MonthlyChargesBucket_Low": 1,
    "MonthlyChargesBucket_Medium": 0
}

response = requests.post(url, json=data)

# Show response
print("Raw Response:", response.text)

try:
    print("Parsed Response:", response.json())
except Exception as e:
    print("Error parsing JSON:", e)

