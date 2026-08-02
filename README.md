# 🎓 Student Grade Predictor

A Machine Learning project that predicts students' final grades based on academic, family, and social factors.

This project demonstrates a complete Machine Learning workflow, starting from data exploration and preprocessing to model evaluation. It also includes a custom implementation of **Linear Regression from scratch using Gradient Descent**, whose performance is compared against Scikit-learn's implementation.

---

## 📖 Project Overview

The objective of this project is to estimate a student's final grade (`G3`) using information about their academic performance, family background, and lifestyle.

The project follows a complete Machine Learning pipeline including:

- Exploratory Data Analysis (EDA)
- Data Preprocessing
- Feature Encoding
- Feature Scaling
- Model Training
- Model Evaluation
- Custom Linear Regression Implementation

---

## 🎯 Problem Statement

Can a student's final grade be predicted using academic, family, and social factors?

This project investigates that question by building and evaluating Linear Regression models using the Student Performance dataset.

---

## 📊 Dataset

**Student Performance Dataset**

- **Samples:** 395 students
- **Features:** 33
- **Target:** `G3` (Final Grade)
- **Task:** Regression

Some important features include:

- Study Time
- Parents' Education
- Family Size
- Parents' Cohabitation Status
- Family Relationship Quality
- Alcohol Consumption
- Travel Time
- Previous Failures
- Internet Access
- Absences

Dataset:

> https://www.kaggle.com/code/mohamedredaibrahim/student-performance-dataset/input

---

## 🛠 Technologies Used

- Python
- NumPy
- Pandas
- Matplotlib
- Scikit-learn
- Jupyter Notebook

---

## ⚙️ Project Pipeline

1. Data Understanding
2. Exploratory Data Analysis (EDA)
3. Data Cleaning
4. Feature Encoding
5. Train/Test Split
6. Feature Scaling
7. Baseline Model using Scikit-learn
8. Linear Regression from Scratch (Gradient Descent)
9. Model Evaluation
10. Performance Comparison

---

## 📈 Results

Both implementations produced equivalent performance metrics, confirming the correctness of the custom Gradient Descent implementation.

Evaluation Metrics:

- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- R² Score

> Numerical results will be added after further experimentation.

---

## 📂 Project Structure

```text
Student_grade_predictor/
│
├── dataset/
│
├── notebooks/
│   ├── 01_eda.ipynb
│   ├── 02_data_preprocessing.ipynb
│   └── 03_training.ipynb
│
├── src/
│   ├── __init__.py
│   └── linear_regression_from_scratch.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🚀 Future Improvements

- Feature Engineering
- Hyperparameter Tuning
- Cross Validation
- Compare with Decision Trees
- Compare with Random Forest
- Compare with Gradient Boosting Models
- Improve Feature Selection
- Build an interactive web application

---

## 👨‍💻 Author

**Abdelrahman Mohamed Saadallah**

Artificial Intelligence Student | Machine Learning Enthusiast