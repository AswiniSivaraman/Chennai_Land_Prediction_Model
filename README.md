# Chennai Land Price Prediction Model

The **Chennai Land Price Prediction Model** is an advanced machine learning project designed to predict the market value of land and properties based on key features such as location, size, and accessibility. By leveraging data preprocessing, exploratory data analysis, and predictive modeling, this solution offers a comprehensive platform for real estate stakeholders to make informed decisions. The project integrates seamlessly with a user-friendly interface, allowing users to input property details and receive accurate price predictions in real time.

---

## Table of Contents

1. [Project Overview](#project-overview)  
2. [Dataset Description](#dataset-description)  
3. [Tools and Technology](#tools-and-technology)  
4. [Project Workflow](#project-workflow)  
5. [Model Development](#model-development)  
6. [Model Deployment](#model-deployment)  
7. [Performance Metrics](#performance-metrics)  
8. [Insights and Learnings](#insights-and-learnings)  
9. [Future Updates](#future-updates)
10. [Installation](#installation)
11. [Streamlit UI](#streamlit-ui)  

---

## Project Overview

This project aims to build a robust machine learning pipeline to predict property prices based on a set of attributes. Property price prediction is a critical component of the real estate sector, influencing decisions related to investments, sales, and urban planning.

The key objectives of the project are:  
- **Accurate Predictions**: Use machine learning algorithms to predict property prices with high accuracy.  
- **User-Friendly Interface**: Deploy the model via a streamlined web application using Streamlit.  

---

## Dataset Description

The dataset contains comprehensive details about properties, including physical attributes, location-based features, and market conditions. Below is a summary:

### Dataset Summary

- **Number of Rows**: ~7,000  
- **Number of Columns**: 22  
- **Target Variable**: `SALES_PRICE` (Property sale price)  

### Dataset Columns

| Column Name       | Description                                      |
|-------------------|--------------------------------------------------|
| `PRT_ID`          | Unique identifier for each property             |
| `AREA`            | Locality or neighborhood where the property is located |
| `INT_SQFT`        | Internal square footage of the property         |
| `DATE_SALE`       | Date of sale transaction                        |
| `DIST_MAINROAD`   | Distance to the nearest main road in meters     |
| `N_BEDROOM`       | Number of bedrooms in the property              |
| `N_BATHROOM`      | Number of bathrooms in the property             |
| `N_ROOM`          | Total number of rooms in the property           |
| `SALE_COND`       | Sale condition (e.g., Normal, Abnormal, Family) |
| `PARK_FACIL`      | Whether parking facility is available (Yes/No)  |
| `DATE_BUILD`      | Construction date of the property               |
| `BUILDTYPE`       | Type of building, such as "Commercial" or "Others" |
| `UTILITY_AVAIL`   | Availability of basic utilities (e.g., AllPub, NoSewr, ELO) |
| `STREET`          | Indicates road access type                     |
| `MZZONE`          | Municipal zoning classification                |
| `QS_ROOMS`        | Quality score for rooms                        |
| `QS_BATHROOM`     | Quality score for bathrooms                    |
| `QS_BEDROOM`      | Quality score for bedrooms                     |
| `QS_OVERALL`      | Overall quality score                          |
| `REG_FEE`         | Registration fees of the property              |
| `COMMIS`          | Commission fees                                |
| `SALES_PRICE`     | Sale price of the property (target variable)    |

---

## Tools and Technology

- **Programming Language**: Python  
- **Core Libraries**:
  - Pandas and NumPy for data handling and manipulation  
  - Matplotlib and Seaborn for visualization  
  - Scikit-learn for model building and evaluation  
- **Web Framework**: Streamlit for interactive deployment  
- **Environment**: Jupyter Notebook for iterative development  

---

## Project Workflow

The project follows a systematic workflow to ensure end-to-end implementation:

1. **Data Understanding**:  
   Load and explore the dataset to understand its structure, types, and key statistics.  

2. **Exploratory Data Analysis (EDA)**:  
   Analyze trends, distributions, and correlations to identify important features.  

3. **Data Cleaning and Preprocessing**:  
   Address missing values, handle outliers, and encode categorical data.  

4. **Feature Engineering**:  
   Create new features or modify existing ones to enhance model performance.  

5. **Model Development**:  
   Train various machine learning algorithms and fine-tune them to achieve optimal performance.  

6. **Model Evaluation**:  
   Assess model accuracy, precision, and recall using appropriate metrics.  

7. **Deployment**:  
   Create an intuitive web application for real-time predictions using Streamlit.  

---

## Model Development

### Algorithms Used

- Linear Regression  
- Ridge Regression  
- Lasso Regression  
- ElasticNet  
- Support Vector Regression (SVR)  
- K-Nearest Neighbors (KNN)  
- Random Forest Regressor  
- Gradient Boosting Regressor  
- Decision Tree Regressor  
- XGBoost  

### Model Selection
The model with the highest R² score and lowest RMSE was selected for deployment.

### Hyperparameter Tuning
Conducted grid search to find the optimal parameters for each algorithm.

---

## Model Deployment

- **User Interface**:  
  Developed using Streamlit for an interactive and visually appealing UI.  

- **Prediction Workflow**:  
  - Users input property details (e.g., location, square footage).  
  - The model processes the inputs and predicts the price in real-time.  

---

## Performance Metrics

- **R² Score**: Measures how well the model predicts the target variable.  
- **MAE (Mean Absolute Error)**: Provides the average magnitude of errors in predictions.  

---

## Insights and Learnings

- Developed a deeper understanding of data preprocessing techniques.  
- Improved skills in hyperparameter tuning and model evaluation.  
- Gained hands-on experience in deploying machine learning models.  

---


## Installation

To set up and run the project, follow these steps:

1. Run the `data_preprocessing.ipynb` notebook by selecting the **Run All** option.    
2. Run the Streamlit app using the following command in the terminal:  
   ```bash
   streamlit run UI_Land_Price_Prediction.py

---

## Future Updates

- Deploy the user interface on AWS for broader accessibility.  

---

## Streamlit UI

Below is an illustration of the Streamlit user interface for this project:

![image](https://github.com/user-attachments/assets/4a5ae51e-b21d-4b04-8a2b-d932c1ddfb8e)

![image](https://github.com/user-attachments/assets/288fd450-4e34-4742-aa9c-cc4d66bf5576)


