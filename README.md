# Mental Health Prediction Using Machine Learning 
An intelligent system for early detection of mental health conditions through machine learning, helping bridge the gap between technology and mental wellness.

## Overview

Mental health challenges affect millions worldwide, yet early detection remains a significant hurdle. This project tackles this problem head-on by implementing a machine learning-based system that can identify potential mental health conditions like depression, anxiety, and stress through user survey responses.

Our web application leverages the power of classification algorithms to provide real-time risk assessments, enabling timely intervention and proactive support for individuals who need it most.

## Tech Stack

**Backend & ML:**
- Python 3.x
- Pandas & NumPy for data manipulation
- scikit-learn for machine learning algorithms
- Flask for web framework
- Pickle for model serialization

**Data Analysis & Visualization:**
- Seaborn & Matplotlib for insightful visualizations
- Jupyter Notebook for exploratory data analysis

**Frontend:**
- HTML/CSS for clean, accessible user interface

**Dataset:**
- [OSMI Mental Health in Tech Survey](https://www.kaggle.com/datasets/osmi/mental-health-in-tech-survey) from Kaggle

## Key Features

- **Smart Data Processing**: Handles missing values, outliers, and categorical encoding automatically
- **Multi-Model Comparison**: Evaluates Decision Tree, Random Forest, and Logistic Regression algorithms
- **Comprehensive Evaluation**: Uses accuracy, precision, recall, F1-score, and confusion matrices
- **Interactive Web Interface**: User-friendly Flask application for real-time predictions
- **Production Ready**: Designed with scalability and explainability in mind
- **Regulatory Awareness**: Built considering healthcare compliance requirements

## Project Structure

```
Mental-Health-Prediction/
├──  data/
│   └── mental_health_survey.csv          # Raw survey dataset
├──  templates/
│   └── index.html                        # Main user interface
├──  static/
│   └── style.css                         # Styling (optional)
├──  app.py                             # Flask backend application
├──  random_forest_model.pkl            # Trained ML model
├──  notebook.ipynb                     # Data analysis & model training
├──  requirements.txt                   # Python dependencies
├──  README.md                          # This documentation
└──  .gitignore                         # Git ignore rules
```

### Directory Breakdown

- **`data/`**: Contains the training and testing datasets
- **`templates/`**: HTML templates for the Flask web interface
- **`static/`**: CSS stylesheets and other static assets
- **`app.py`**: Main Flask application with prediction logic
- **`random_forest_model.pkl`**: Serialized best-performing model
- **`notebook.ipynb`**: Complete data exploration and model development workflow


### Prerequisites
Make sure you have Python 3.x installed on your system.

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/Mental-Health-Prediction.git
   cd Mental-Health-Prediction
   ```

2. **Install required packages:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Download the dataset:**
   - Visit [Kaggle OSMI Mental Health Survey](https://www.kaggle.com/datasets/osmi/mental-health-in-tech-survey)
   - Download the CSV file and place it in the `data/` directory

4. **Explore the data (optional):**
   ```bash
   jupyter notebook notebook.ipynb
   ```

5. **Launch the application:**
   ```bash
   python app.py
   ```
   
   Navigate to `http://127.0.0.1:5000` in your web browser.

## Model Performance

We rigorously evaluated multiple algorithms to ensure reliable predictions:

| Algorithm | Accuracy | Precision | Recall | F1-Score |
|-----------|----------|-----------|---------|----------|
| Random Forest |  Best |  Best |  Best |  Best |
| Decision Tree | Good | Good | Good | Good |
| Logistic Regression | Moderate | Moderate | Moderate | Moderate |

**Why Random Forest?**
- Superior handling of mixed data types
- Built-in feature importance ranking
- Robust against overfitting
- Excellent performance on imbalanced datasets

##  Important Notes

- This tool is designed for **screening and awareness purposes only**
- It should **never replace professional medical advice**
- Always consult qualified healthcare providers for proper diagnosis and treatment
- The model's predictions are based on survey data and may not capture all individual circumstances

## References & Acknowledgments

- **Dataset**: [OSMI Mental Health in Tech Survey](https://www.kaggle.com/datasets/osmi/mental-health-in-tech-survey)
- **ML Framework**: [scikit-learn documentation](https://scikit-learn.org/)
- **Web Framework**: [Flask documentation](https://flask.palletsprojects.com/)
- **Inspiration**: Industry best practices in healthcare ML applications
