from flask import Flask, render_template, request, redirect, url_for
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load your trained ML model
with open(r'flask\random_forest_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Define feature names in correct order
FEATURES = [
    "Age", "Gender", "self_employed", "family_history", "work_interfere",
    "no_employees", "remote_work", "tech_company", "benefits", "care_options", "wellness_program",
    "seek_help", "anonymity", "leave", "mental_health_consequence", "phys_health_consequence",
    "coworkers", "supervisor", "mental_health_interview", "phys_health_interview",
    "mental_vs_physical", "obs_consequence"
]

# Basic mappings — extend as per your model's training encoding
simple_map = {
    "Yes": 1, "No": 0, "Maybe": 2, "Don't know": 3, "Not sure": 3,
    "Very easy": 1, "Somewhat easy": 2, "Somewhat difficult": 3, "Very difficult": 4
}

multi_map = {
    "work_interfere": {"Never": 0, "Rarely": 1, "Sometimes": 2, "Often": 3},
    "leave": {"Very easy": 1, "Somewhat easy": 2, "Somewhat difficult": 3, "Very difficult": 4, "Don't know": 0},
    "coworkers": {"Yes": 1, "No": 0, "Some of them": 2},
    "supervisor": {"Yes": 1, "No": 0, "Some of them": 2},
    "mental_health_interview": {"Yes": 1, "No": 0, "Maybe": 2},
    "phys_health_interview": {"Yes": 1, "No": 0, "Maybe": 2},
    "mental_vs_physical": {"Yes": 1, "No": 0, "Don't know": 2},
    "obs_consequence": {"Yes": 1, "No": 0, "Maybe": 2},
    "mental_health_consequence": {"Yes": 1, "No": 0, "Maybe": 2},
    "phys_health_consequence": {"Yes": 1, "No": 0, "Maybe": 2},
}

# Homepage
@app.route('/')
def home():
    return render_template('home.html')

# Prediction form
@app.route('/predict')
def predict_form():
    return render_template('index.html')

# Submit and predict
@app.route('/submit', methods=['POST'])
def submit():
    user_input = {}

    for feature in FEATURES:
        value = request.form.get(feature)
        if feature == "Age":
            user_input[feature] = int(value)
        elif feature in multi_map:
            user_input[feature] = multi_map[feature].get(value, 0)
        else:
            user_input[feature] = simple_map.get(value, 0)

    # Convert to DataFrame for model input
    input_df = pd.DataFrame([user_input])[FEATURES]

    # Predict
    prediction = model.predict(input_df)[0]  # assume 1 = needs treatment

    result = 'yes' if prediction == 1 else 'no'
    return redirect(url_for('output', result=result))

# Output
@app.route('/output')
def output():
    result = request.args.get('result')
    return render_template('output.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
