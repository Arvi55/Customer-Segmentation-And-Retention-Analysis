# 📊 Customer Segmentation & Churn Prediction
##  End-to-end Data Analytics + Machine Learning project combining Power BI and Streamlit.

This project combines **customer behavior analysis** and **machine learning** to identify high-value customers and predict churn risk.

It integrates:
- 📊 Power BI Dashboard (Customer Segmentation)
- 🤖 Machine Learning Model (Churn Prediction)
- 🌐 Streamlit Web App (Deployment)

---

# Project Background

Customer retention is crucial for business growth. This project analyzes transactional data to:

- Segment customers using **RFM analysis**
- Identify **high-value customers**
- Detect **customers at risk of churn**
- Build a predictive model for churn

---

# Analysis Approach

The project follows a structured workflow:

- Data cleaning and preprocessing  
- Feature engineering (RFM metrics)  
- Exploratory Data Analysis  
- Customer segmentation  
- Dashboard creation (Power BI)  
- Business insights & recommendations  

---

# 🗂️ Data Structure

Dataset includes:

- **CustomerID** → Unique identifier  
- **InvoiceDate** → Transaction date  
- **Quantity** → Number of items  
- **UnitPrice** → Price per item  

### 🔍 Derived Features:

- **Recency** → Days since last purchase  
- **Frequency** → Number of purchases  
- **Monetary** → Total spend  

---

# 🔍 Data Cleaning & Preprocessing

- Removed missing Customer IDs  
- Filtered cancelled/negative transactions  
- Created total revenue column  
- Aggregated data at customer level  
- Calculated RFM metrics (Recency, Frequency, Monetary)

---

# 📊 Dashboard Overview

![Dashboard Overview](https://github.com/Arvi55/Customer-Segmentation-And-Retention-Analysis/blob/main/Images/Page3.png?raw=true)



---

# 📈 Executive Summary

## 🔍 Key Insights

- ~65% of revenue comes from **Champions segment**
- Only ~36% of customers contribute majority of revenue  
- ~7% revenue is at risk from churn-prone segments  
- Retention rate is high (~88%) but risk is concentrated  

---

# 📊 Revenue Contribution Analysis

![Revenue Contribution](https://github.com/Arvi55/Customer-Segmentation-And-Retention-Analysis/blob/main/Images/Revenue%20Contribution.png?raw=true)



### Insights:

- Champions contribute the largest share (~65%)  
- Loyal and Big Spenders contribute moderate revenue  
- At Risk and Hibernating contribute less but are critical  

---

# ⚠️ Revenue Risk Analysis

![Revenue Risk](https://github.com/Arvi55/Customer-Segmentation-And-Retention-Analysis/blob/main/Images/Revenue%20Risk.png?raw=true)



### Insights:

- ~40% of at-risk revenue comes from:
  - At Risk customers  
  - Hibernating customers  
- These segments require immediate intervention  

---

# 📉 Customer Distribution Analysis

![Distribution](https://github.com/Arvi55/Customer-Segmentation-And-Retention-Analysis/blob/main/Images/Distribution.png?raw=true)



### Insights:

- Recency shows many inactive customers  
- Frequency is highly skewed → few loyal customers  
- Monetary follows long-tail distribution  

---

# 📊 Segment-Level Analysis

![Segment Analysis](https://github.com/Arvi55/Customer-Segmentation-And-Retention-Analysis/blob/main/Images/Segment%20Analysis.png?raw=true)



### Insights:

- Champions have high frequency & monetary  
- At Risk customers show high recency  
- Clear separation between segments  

---

# 📈 Time-Based Analysis

![Time Trend](https://github.com/Arvi55/Customer-Segmentation-And-Retention-Analysis/blob/main/Images/Time%20Trend.png?raw=true)



### Insights:

- Revenue shows growth trend over time  
- Order volume increases seasonally  
- Indicates business expansion  

---

# 🌍 Geographic Analysis

![Country Revenue](https://github.com/Arvi55/Customer-Segmentation-And-Retention-Analysis/blob/main/Images/Country%20Revenue.png?raw=true)



### Insights:

- Majority revenue comes from one dominant region  
- Other countries contribute marginally  

---

# 🏁 Key Results

- 🟢 High-value customers drive most revenue  
- 🔴 At-risk segments indicate churn signals  
- 📉 Engagement strongly affects retention  
- 🎯 Small segment contributes disproportionately  

---

# 💡 Business Recommendations

- Target **At Risk customers** with offers  
- Reward **Champions & Loyal customers**  
- Re-engage inactive users  
- Increase purchase frequency  
- Focus on retention strategies  

---

# 🤖 Machine Learning: Customer Churn Prediction

## 📌 Overview

A Machine Learning model was built to predict customer churn using RFM features.

## 🌐 Live Demo

👉 [Click here to try the app](https://avinash-customer-segmentation-and-retention-analysis.streamlit.app/)

![Web Image](https://github.com/Arvi55/Customer-Segmentation-And-Retention-Analysis/blob/main/Images/WEB%20IMAGE.png?raw=true)   

---

## 🧩 Problem Statement

- Identify customers likely to churn  
- Improve retention strategies  
- Support decision making  

---

## 📂 Features Used

- Recency  
- Frequency  
- Monetary  

---

## 🧠 Model Selection

Models tested:
- Logistic Regression  
- Random Forest ✅ (selected)

### Why Random Forest?
- Handles non-linear patterns  
- Works well on structured data  
- Better performance  

---

## ⚙️ Model Training

- Train-test split (80/20)  
- Class balancing applied  
- Evaluated using multiple metrics  

---

## 📊 Evaluation Metrics

- Accuracy  
- Precision  
- Recall  
- ROC-AUC  

👉 Focus was on **Recall (churn detection)**

---

## 📈 Prediction Logic

- Used probability-based prediction  
- Applied custom threshold tuning  

---

## 🌐 Web App (Streamlit)

The model is deployed as an interactive app where users can:

- Enter customer data  
- Get churn prediction  
- View probability and risk level  

---

## 📈 Key Observations

- Recency is strongest churn indicator  
- Low engagement increases churn risk  
- Model behavior depends on data patterns  

---

## 🛠️ Tech Stack

- Python  
- Pandas, NumPy  
- Scikit-learn  
- Power BI  
- Streamlit  

---

## 🚀 Future Improvements

- Use real-world churn labels  
- Add more behavioral features  
- Try advanced models (XGBoost)  
- Deploy online  

---

## 🏁 Conclusion

This project demonstrates how:

- Data analysis → identifies patterns  
- Machine learning → predicts behavior  
- Visualization → supports decisions  

Together, they create a complete **data-driven retention system**.

---

## 📌 Interview One-Liner

I built an end-to-end customer analytics solution using Power BI and Machine Learning to segment customers and predict churn, enabling data-driven retention strategies.
