# PayInsight

# 💳 PayInsight: End-to-End Payment Analytics Platform

## 🚀 Overview

PayInsight is a complete end-to-end data engineering and analytics project built using **Databricks (PySpark)** and **Streamlit**.
The system processes raw payment data, transforms it using Medallion Architecture (Bronze → Silver → Gold), and provides interactive business insights through a web dashboard.

---

## 🧱 Architecture

```
Data Source → Bronze Layer → Silver Layer → Gold Layer → Streamlit Dashboard
```

* **Bronze Layer**: Raw data ingestion
* **Silver Layer**: Data cleaning and transformation
* **Gold Layer**: Business KPIs and analytics-ready tables
* **Frontend**: Streamlit dashboard for visualization

---

## ⚙️ Tech Stack

* 🔹 Databricks
* 🔹 PySpark
* 🔹 Delta Lake
* 🔹 Python
* 🔹 Streamlit
* 🔹 Pandas & Matplotlib

---

## 📊 Features

* 📈 Daily Revenue Analysis
* 💳 Payment Method Insights (UPI, Card, Wallet)
* ⚠️ Failure Analysis
* 👤 Customer Lifetime Value Analysis
* 📊 Interactive Dashboard with Filters
* 📥 Downloadable Reports

---

## 🗂️ Project Structure

```
payment-analytics-dashboard/
│
├── app.py                   # Streamlit dashboard
     
├── requirements.txt

├── data/                    # Gold layer exported data
        
│   ├── daily_revenue.csv

│   ├── payment_method_kpi.csv

│   ├── customer_360.csv

│   ├── payment_failures.csv
│
└── databricks/

    ├── bronze_layer.py

    ├── silver_layer.py

    ├── gold_layer.py
```

---

## 🔄 Data Pipeline (Databricks)

### Bronze Layer

* Raw data ingestion
* Added ingestion timestamp

### Silver Layer

* Removed duplicates
* Handled null values
* Standardized payment status

### Gold Layer

* Created fact table
* Generated KPI tables:

  * Daily Revenue
  * Payment Method KPIs
  * Customer 360
  * Failure Analysis

---

## ▶️ How to Run Locally

### 1. Clone Repository

```
git clone https://github.com/your-username/payment-analytics-dashboard.git
cd payment-analytics-dashboard
```

### 2. Install Dependencies

```
pip install -r requirements.txt
```

### 3. Run Streamlit App

```
streamlit run app.py
```

---

## 🌐 Live Demo

(After deployment, add your Streamlit link here)

---

## 🧠 Key Insights

* UPI dominates transaction volume
* Card payments show higher failure rates
* Revenue trends vary across dates
* High-value customers contribute significantly to revenue

---

## 🎯 Future Enhancements

* Real-time data integration with Databricks
* Payment failure prediction using ML
* API-based data ingestion
* Advanced dashboard filters

---

## 👩‍💻 Author

Monika

---

## ⭐ If you like this project, give it a star!
