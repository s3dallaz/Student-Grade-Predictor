# 🎓 Student Grade Predictor

A complete Machine Learning project that predicts students' final grades using academic, family, and social factors.

This project covers the complete Machine Learning workflow, from Exploratory Data Analysis (EDA) and data preprocessing to building a custom Linear Regression model from scratch using Gradient Descent and comparing it with Scikit-learn's implementation.

---

# ⭐ Project Highlights

- Built **Linear Regression from Scratch** using Gradient Descent.
- Compared the custom implementation with **Scikit-learn**.
- Created reusable preprocessing functions inside `src/`.
- Performed complete Exploratory Data Analysis (EDA).
- Evaluated the model using multiple regression metrics.
- Visualized both the learning process and model performance.

---

# 🎯 Problem Statement

Can a student's final grade be predicted using academic, family, and social factors?

The objective of this project is to build a regression model capable of estimating students' final grades using features such as:

- Study time
- Parents' education
- Family relationships
- Alcohol consumption
- Travel time
- Previous grades
- Family support
- ...and many other factors.

---

# 📊 Dataset

**Dataset:** Student Performance Dataset

- Samples: **395**
- Features: **33**
- Target: **G3 (Final Grade)**
- Task: **Regression**

The dataset contains demographic, educational, family, and lifestyle information collected from Portuguese secondary school students.

Kaggle Dataset:

https://www.kaggle.com/code/mohamedredaibrahim/student-performance-dataset/input

---

# 📂 Project Structure

```text
Student_grade_predictor/
│
├── assets/
│   ├── cost_vs_epochs.png
│   ├── actual_vs_predicted.png
│   └── residual_plot.png
│
├── dataset/
│
├── notebooks/
│   ├── 01_EDA.ipynb
│   ├── 02_Data_Preprocessing.ipynb
│   └── 03_Model_Training.ipynb
│
├── src/
│   ├── preprocessing.py
│   ├── linear_regression_from_scratch.py
│   └── __init__.py
│
├── README.md
└── requirements.txt
```

---

# ⚙️ Machine Learning Pipeline

```
Problem
    ↓
Dataset
    ↓
Exploratory Data Analysis
    ↓
Data Preprocessing
    ↓
Feature Encoding
    ↓
Feature Scaling
    ↓
Train / Test Split
    ↓
Model Training
    ↓
Model Evaluation
    ↓
Model Analysis
    ↓
Documentation
```

---

# 🛠 Technologies Used

- Python
- NumPy
- Pandas
- Matplotlib
- Scikit-learn
- Jupyter Notebook

---

# 🤖 Models

### Scikit-learn

Used as the baseline implementation.

### Linear Regression From Scratch

Implemented from scratch using:

- Gradient Descent
- Mean Squared Error (MSE) Cost Function
- Analytical Gradient Computation

---

# 📈 Evaluation Metrics

The model was evaluated using:

- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- R² Score

The custom implementation achieved results very close to Scikit-learn's implementation.

---

# 📊 Model Visualizations

## 1. Cost vs Epochs

![Cost vs Epochs](assets/cost_vs_epochs.png)

The training cost decreases rapidly during the early epochs before gradually stabilizing.

After experimenting with **10,000 epochs**, no meaningful improvement in the cost was observed compared to **300 epochs**. The additional epochs only increased the training time, making **300 epochs** a more efficient choice for this project.

---

## 2. Actual vs Predicted

![Actual vs Predicted](assets/actual_vs_predicted.png)

Most predictions lie close to the ideal prediction line, indicating that the model successfully captures the relationship between the input features and the students' final grades.

The largest prediction errors mainly occur for students with extremely low grades.

---

## 3. Residual Plot

![Residual Plot](assets/residual_plot.png)

The residuals are randomly distributed around zero without a noticeable pattern.

This suggests that the Linear Regression model is appropriate for the dataset and does not exhibit obvious systematic prediction errors.

---

# 📋 Conclusions

This project demonstrates the complete Machine Learning workflow for a regression problem.

Key takeaways include:

- Understanding the dataset through EDA.
- Building reusable preprocessing functions.
- Implementing Linear Regression from scratch.
- Comparing the custom implementation with Scikit-learn.
- Using visualizations to analyze both the learning process and prediction quality.

---

# 🚀 Future Improvements

Possible future enhancements include:

- Feature Engineering
- Hyperparameter Tuning
- Cross Validation
- Polynomial Regression
- Decision Tree Regressor
- Random Forest Regressor
- XGBoost Regressor

---

# ▶️ How to Run

```bash
git clone <repository-url>

cd Student_grade_predictor

pip install -r requirements.txt
```

Run the notebooks in the following order:

1. EDA
2. Data Preprocessing
3. Model Training

---

# 👨‍💻 Author

Abdelrahman Mohamed Saadallah

AI Student | Machine Learning Enthusiast