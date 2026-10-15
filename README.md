# Phishing URL Detection using SVM

A machine learning project that detects whether a URL is **phishing** or **benign** using a Support Vector Machine (SVM) classifier.

The project includes data preprocessing, exploratory data analysis, feature engineering, SVM model training and tuning, model evaluation, and a Streamlit web application for prediction.

## Project Overview

Phishing websites are designed to deceive users into providing sensitive information such as login credentials, financial information, or personal data.

This project uses URL and webpage-related features to classify URLs into two categories:

* **Phishing**
* **Benign**

A Support Vector Machine with an RBF kernel is used as the final classification model.

## Dataset

Dataset Source: Phishing URL Content Dataset — Kaggle, by Aaditey Pillai.
The dataset used in this project was preprocessed and feature-engineered for SVM classification. The processed dataset contains 800 records and 24 columns.
The dataset contains **800 records** and **24 features** related to URLs and webpage characteristics.

Some of the features include:

* Link Density
* External Links
* Internal Links
* External IP Count
* HTTP/HTTPS Counts
* Iframe Counts
* HTTPS Indicator
* Certificate Validity Days
* Domain Validity Days
* URL Length
* Number of Dots
* Number of Hyphens
* Number of Slashes
* Number of Digits
* Special Characters
* URL Has IP
* Country
* Organization
* Certificate
* Whois Country

The target variable contains two classes:

* `phishing`
* `benign`

> **Note:** The dataset was obtained from Kaggle and is used for educational and project purposes.


## Machine Learning Workflow

The project follows these steps:

1. Load the dataset
2. Explore the dataset
3. Handle missing values
4. Perform exploratory data analysis
5. Prepare numerical and categorical features
6. Encode categorical variables
7. Scale numerical features
8. Split the data into training and testing sets
9. Train SVM models using different kernels
10. Tune hyperparameters using GridSearchCV
11. Evaluate the final model
12. Save the trained model and preprocessing components
13. Build a Streamlit application for prediction

## Model

Support Vector Machine (SVM) was selected for classification.

Different kernels were evaluated:

* Linear
* RBF
* Polynomial

Hyperparameter tuning was performed using `GridSearchCV`.

### Best Parameters

- Kernel: RBF
- C: 100
- Gamma: auto

## Model Performance

The tuned SVM model achieved the following results on the test set:

| Metric    |   Score |
| --------- | ------: |
| Accuracy  |  98.11% |
| Precision |  96.39% |
| Recall    | 100.00% |
| F1 Score  |  98.16% |
| ROC-AUC   |  99.62% |

The model's performance is based on the test split used during the project and should not be interpreted as a guarantee of performance on unseen real-world URLs.

## Streamlit Application

The project includes a Streamlit web application that allows users to enter URL-related information and obtain a prediction.

The application contains pages for:

* **Model Prediction**
* **Data Analysis**

If your system has multiple Python installations, make sure Streamlit and the required packages are installed in the same Python environment used to run the application.


## Important Note

This project is intended for **educational and demonstration purposes**. It should not be considered a complete cybersecurity solution or used as the sole method for determining whether a website is safe.


