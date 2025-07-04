# Customer Churn Prediction Project

This project is an **end-to-end Machine Learning pipeline** that predicts customer churn using telecom service data. It includes:

-  A trained ML model built with Logistic Regression
-  A Flask API to serve predictions in real-time
-  A Streamlit dashboard for interactive user inputs
-  A test client to send sample prediction requests
-  Fully reproducible with requirements.txt and clean project structure

---

### Live Dashboard (Streamlit)
Deployed via ngrok — run this locally or in Colab to test live prediction:

# Streamlit launch example (Colab or local)
streamlit run streamlit_app.py

Features
Predict customer churn with a trained ML model

Accepts JSON input via REST API (/predict)

Streamlit UI for easy manual input

Scales input using pre-saved scaler.pkl

Works both locally and in Google Colab


Tech Stack

| Component      | Library Used                |
| -------------- | --------------------------- |
| Model Training | scikit-learn, pandas, numpy |
| API            | Flask, requests             |
| Dashboard      | Streamlit                   |
| Deployment     | pyngrok (for Colab tunnel)  |
| Packaging      | requirements.txt            |

Project Structure

churn-prediction-project/
├── api/
│   ├── main.py               # Flask API for churn prediction
│   ├── test_client.py        # Sends sample request to API
│   ├── scaler.pkl            # Scaler used to transform input
│   └── churn_model.pkl       # Trained ML model
├── dashboard/
│   └── streamlit_app.py      # Streamlit dashboard
├── notebooks/
│   └── churn_model_training.ipynb 
├── requirements.txt          # All required Python libraries
└── README.md                 # Project overview (this file)

Getting Started
Step 1: Clone the repository
git clone https://github.com/your-username/churn-prediction-project.git
cd churn-prediction-project

Step 2: Install dependencies
pip install -r requirements.txt

Step 3: Run the Flask API
cd api
python main.py

The API will start on http://localhost:8080

Test it using:
python test_client.py

Step 4: Launch Streamlit Dashboard
cd dashboard
streamlit run streamlit_app.py

If using Google Colab, you can expose your Streamlit app with pyngrok:

from pyngrok import ngrok
ngrok.set_auth_token("YOUR_AUTHTOKEN_HERE")
public_url = ngrok.connect(8501)
print("Dashboard URL:", public_url)

Example API Input (JSON)

{
  "SeniorCitizen": 0,
  "Partner": 1,
  "Dependents": 0,
  "tenure": 5,
  "PhoneService": 1,
  "PaperlessBilling": 0,
  "MonthlyCharges": 29.85,
  "TotalCharges": 298.5,
  "ServiceCount": 3,
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


Future Improvements

Deploy API to Render / Railway
Dockerize the project
Add CI/CD + unit tests
Switch model to XGBoost or ensemble

## Author
Built by Manoj Kumar
GitHub: https://github.com/manojkumar5666

## License

This project is licensed under the [MIT License](LICENSE.md).

