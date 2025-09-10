Mental-Health-Prediction/
├── data/
│   └── mental_health_survey.csv         # Raw dataset downloaded from Kaggle
├── templates/
│   └── index.html                       # Main HTML file for user interface
├── static/
│   └── style.css                        # (Optional) CSS styling for the web app
├── app.py                               # Flask web server and model inference logic
├── random_forest_model.pkl              # Best trained ML model (serialized)
├── notebook.ipynb                       # Jupyter notebook for EDA, preprocessing, and model training
├── requirements.txt                     # List of required Python dependencies
├── README.md                            # Project documentation and usage guide
└── .gitignore                           # Files/patterns to be ignored by Git

Mental Health Prediction Using Machine Learning
Overview
This project implements a machine learning-based system for the early detection of mental health conditions like depression, anxiety, or stress. The web application uses user survey responses and makes predictions using trained classification models, empowering timely intervention and proactive support for at-risk individuals.

Tech Stack
Python 3.x

Pandas, NumPy, scikit-learn (data manipulation, ML algorithms)

Seaborn, Matplotlib (visualization)

Flask (web app framework)

HTML/CSS (UI/Frontend)

Pickle (model serialization)

Jupyter Notebook (EDA and ML development)

Dataset: Kaggle [OSMI Mental Health in Tech Survey]

Features
Cleans and preprocesses survey data (missing value imputation, outlier visualization, categorical encoding)

Trains and compares multiple ML models (Decision Tree, Random Forest, Logistic Regression) for prediction

Evaluates models with accuracy, precision, recall, F1-score, and confusion matrix

Interactive Flask web app for user input and real-time prediction

Regulatory-aware and designed for scalability and explainability
