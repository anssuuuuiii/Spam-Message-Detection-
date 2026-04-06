# 📧 Email Spam Detection using Machine Learning

## 📌 Project Overview

This project focuses on building a **machine learning model** to classify emails as **Spam** or **Not Spam (Ham)**.
It uses **Natural Language Processing (NLP)** techniques to convert text data into numerical features and applies classification algorithms to make predictions.

---

## 🎯 Objectives

* Detect spam emails automatically
* Compare performance of different ML models
* Build a simple UI for real-time prediction

---

## 🧰 Technologies & Libraries Used

* **Python**
* **Pandas** → Data handling
* **NumPy** → Numerical operations
* **Matplotlib & Seaborn** → Data visualization
* **NLTK** → Text preprocessing (stopwords removal)
* **Scikit-learn** → Machine learning models and evaluation

---

## ⚙️ Methods & Workflow

### 1. Data Preprocessing

* Converted text to lowercase
* Removed special characters using regex
* Tokenized text into words
* Removed stopwords using NLTK

---

### 2. Feature Extraction

* Used **TF-IDF (Term Frequency - Inverse Document Frequency)**
* Converted text data into numerical vectors

---

### 3. Model Training

Two models were implemented:

#### 🔹 Naïve Bayes

* Suitable for text classification
* Fast and efficient

#### 🔹 Logistic Regression

* Provides better accuracy in many cases
* Handles feature relationships better

---

### 4. Model Evaluation

* Accuracy Score
* Classification Report
* Confusion Matrix

---

## 📊 Results

### ✅ Model Accuracy

* **Naïve Bayes Accuracy:** 0.9781849912739965
* **Logistic Regression Accuracy:** 0.9790575916230366

---

### 📋 Classification Report

```
              precision    recall  f1-score   support

           0       0.98      1.00      0.99       856
           1       0.99      0.93      0.96       290

    accuracy                           0.98      1146
   macro avg       0.98      0.96      0.97      1146
weighted avg       0.98      0.98      0.98      1146
```

---

## 📈 Visualization

### 🔹 Spam vs Ham Distribution

<img width="580" height="455" alt="image" src="https://github.com/user-attachments/assets/c86b9e09-b3e2-4f74-8f9b-a062eee44393" />


---

### 🔹 Confusion Matrix

<img width="539" height="455" alt="image" src="https://github.com/user-attachments/assets/57df03d6-67b6-4a76-89e4-4576d7548e5b" />


---

## 🧪 Example Prediction

Input:

```
"Congratulations! You have won a free prize"
```

Output:

```
Spam
```

---

## 🖥️ User Interface

A simple **Streamlit web application** was developed where users can:

* Enter email text
* Get instant prediction (Spam / Not Spam)

---

## 🚀 Future Improvements

* Use advanced models like **SVM or Random Forest**
* Improve accuracy using **hyperparameter tuning**
* Deploy application online
* Add real-time email filtering

---

## 🧠 Conclusion

The project successfully demonstrates how **machine learning and NLP** can be used to detect spam emails with high accuracy.
Logistic Regression slightly outperformed Naïve Bayes in this case.

---

## 👨‍💻 Author

Debidatta Pattanaik

