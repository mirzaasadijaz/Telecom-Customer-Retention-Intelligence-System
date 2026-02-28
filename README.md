# Telecom Customer Retention Intelligence System 📡📉
This repository features a complete, end-to-end Machine Learning pipeline designed to predict customer churn in the telecommunications industry. The project spans from raw data normalization using SQL, through exploratory data analysis and model training in Python, all the way to a fully deployed interactive web application using Streamlit.

# 🚀 Project Overview
Customer churn is a critical metric for subscription-based services. This project aims to proactively identify customers who are at high risk of canceling their subscriptions. By analyzing demographics, account information, and service usage, the Random Forest model calculates a "Churn Probability," allowing businesses to target at-risk customers with retention strategies.

# 📊 Key Features & Pipeline Breakdown
## 1. Data Engineering & Database Design (sql_data.sql)
Transformed the flat raw CSV data into a relational database structure (telco_project_db).

Normalized the data into distinct tables: Customers (demographics), Services (product details), and Billing (financials & churn status).

Established Primary Keys (customer_id) to prepare the architecture for advanced BI tool integrations (like Power BI or Tableau).

## 2. Machine Learning Model (Telecom Customer Retention...ipynb)
Data Preprocessing: Handled categorical variables using One-Hot Encoding and scaled numerical features.

Model Training: Developed a highly accurate Random Forest Classifier to predict churn.

Artifact Generation: Serialized the trained model (churn_model.pkl) and the exact feature columns (model_columns.pkl) to ensure perfect alignment between the training environment and the production app.

Batch Prediction: Scored the entire dataset and exported the probabilities to customer_churn_predictions.csv for further analysis.

## 3. Interactive Web Application (app.py)
Built a front-end UI using Streamlit.

Users can input customer parameters (Tenure, Monthly Charges, Contract Type, etc.) via intuitive sliders and dropdowns.

The app dynamically preprocesses the user input, aligns it with the trained model's expected columns, and outputs a real-time Churn Probability metric and classification.

# 🛠️ Tech Stack & Libraries
Language: Python 3, SQL

Web Framework: Streamlit

Machine Learning: Scikit-Learn (Random Forest)

Data Manipulation: Pandas, NumPy

Serialization: Pickle
