from flask import Flask, request, jsonify
import joblib
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load model & scaler
model = joblib.load('churn_model.pkl')
scaler = joblib.load('scaler.pkl')

@app.route('/')
def home():
    return "🎉 Welcome to the Churn Prediction API! Use /predict with POST JSON."

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Load input data
        data = request.get_json()
        df = pd.DataFrame([data])

        # Scale
        scaled = scaler.transform(df)

        # Predict
        pred = model.predict(scaled)[0]
        prob = model.predict_proba(scaled)[0][1]

        return jsonify({
            "Churn": "Yes" if pred == 1 else "No",
            "Churn_Probability": round(float(prob), 4)
        })

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
