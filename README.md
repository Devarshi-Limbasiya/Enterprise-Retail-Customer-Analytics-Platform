# 📊 Enterprise Retail Customer Analytics Platform

<p align="center">
  <img src="architecture/project_architecture.png" width="900">
</p>

<p align="center">

![Python](https://img.shields.io/badge/Python-3.10-blue)
![SQL Server](https://img.shields.io/badge/SQL%20Server-TSQL-red)
![PowerBI](https://img.shields.io/badge/PowerBI-Dashboard-yellow)
![Scikit-Learn](https://img.shields.io/badge/Machine%20Learning-Scikit--Learn-orange)
![Pandas](https://img.shields.io/badge/Data%20Analysis-Pandas-green)
![Status](https://img.shields.io/badge/Status-Completed-success)

</p>

---

# 📌 Project Overview

The **Enterprise Retail Customer Analytics Platform** is an end-to-end customer analytics and business intelligence solution developed using **SQL Server, Python, Machine Learning, and Power BI**.

The project integrates:

- Enterprise Data Warehouse Development
- Exploratory Data Analysis (EDA)
- Customer Segmentation
- Customer Lifetime Value Analysis
- Customer Retention Cohort Analysis
- Customer Churn Prediction
- Sales Forecasting
- Interactive Business Intelligence Dashboards

The objective of this project is to transform raw retail transaction data into actionable business insights that support customer retention, revenue growth, and strategic decision-making.

---

# 🚀 Business Objectives

This project addresses the following business problems:

✅ Identify high-value customers

✅ Segment customers based on purchasing behavior

✅ Predict customer churn risk

✅ Forecast future sales revenue

✅ Analyze customer retention patterns

✅ Calculate customer lifetime value

✅ Develop executive business dashboards

✅ Build an enterprise-grade retail analytics ecosystem

---

# 🏗️ System Architecture

<p align="center">
  <img src="architecture/project_architecture.png" width="1000">
</p>

The architecture follows a layered analytics approach:

```
Raw Data Sources
        ↓
SQL Server Data Warehouse
        ↓
Data Processing & ETL Pipelines
        ↓
Python Analytics Layer
        ↓
Machine Learning Models
        ↓
Power BI Executive Dashboard
```

---

# 🛠️ Technology Stack

| Category | Technology |
|----------|------------|
| Database | SQL Server |
| Programming | Python |
| Data Analysis | Pandas |
| Machine Learning | Scikit-Learn |
| Visualization | Power BI |
| Notebook Environment | Google Colab |
| Version Control | Git & GitHub |
| ETL | SQL ETL Pipelines |

---

# 📂 Repository Structure

```text
Enterprise-Retail-Customer-Analytics-Platform/

├── architecture/
├── dashboard/
├── datasets/
├── database/
├── scripts/
├── notebooks/
├── outputs/
├── docs/
├── requirements.txt
├── README.md
└── LICENSE
```

---

# 🗄️ Data Warehouse Architecture

The project follows a multi-layer warehouse design:

### Bronze Layer
Raw CRM and ERP datasets.

### Silver Layer
Cleaned, standardized and transformed datasets.

### Gold Layer
Business-ready analytical datasets and reporting tables.

### Star Schema

- Fact Table:
  - fact_sales

- Dimension Tables:
  - dim_customers
  - dim_products
  - dim_dates

---

# 📈 Exploratory Data Analysis

## Annual Sales Revenue

<p align="center">
<img src="outputs/visualizations/eda/sales_by_year.png" width="700">
</p>

---

## Top Countries by Sales Revenue

<p align="center">
<img src="outputs/visualizations/eda/top_countries.png" width="700">
</p>

---

# 👥 Customer RFM Analysis

RFM analysis was performed to understand customer purchasing behavior.

- Recency
- Frequency
- Monetary Value

## Customer Recency Distribution

<p align="center">
<img src="outputs/analytics/rfm_recency_distribution.png" width="700">
</p>

---

## Frequency vs Monetary Value

<p align="center">
<img src="outputs/visualizations/rfm/rfm_frequency_monetary.png" width="700">
</p>

---

## Customer Segments

<p align="center">
<img src="outputs/rfm_segments.png" width="700">
</p>

---

# 💰 Customer Lifetime Value Analysis

Customer Lifetime Value (CLV) was calculated to identify long-term customer profitability.

## CLV Distribution

<p align="center">
<img src="outputs/visualizations/clv/clv_distribution.png" width="700">
</p>

---

## Top Customers by CLV

<p align="center">
<img src="outputs/visualizations/clv/top_customers_clv.png" width="700">
</p>

---

# 🔄 Customer Cohort Retention Analysis

Customer retention patterns were analyzed using cohort analysis.

<p align="center">
<img src="outputs/visualizations/cohort/cohort_retention_heatmap.png" width="900">
</p>

---

# 🧠 Customer Segmentation

K-Means clustering was applied to segment customers according to purchasing behavior.

<p align="center">
<img src="outputs/visualizations/segmentation/customer_segmentation_clusters.png" width="800">
</p>

---

# ⚠️ Customer Churn Prediction

A machine learning model was developed to predict customer churn behavior.

<p align="center">
<img src="outputs/visualizations/churn/customer_churn_feature_importance.png" width="700">
</p>

---

# 📈 Sales Forecasting

Future sales revenue was forecasted using historical sales patterns.

## Historical Sales Trend

<p align="center">
<img src="outputs/visualizations/forecasting/monthly_sales_trend.png" width="700">
</p>

---

## Forecasted Sales Revenue

<p align="center">
<img src="outputs/visualizations/forecasting/sales_forecasting_prediction.png" width="900">
</p>

---

# 📊 Power BI Dashboard

An executive-level Power BI dashboard was developed to provide:

- Revenue Analysis
- Customer Analysis
- Product Analysis
- Sales Trends
- Geographic Insights
- Customer Segmentation
- KPI Monitoring

<p align="center">
<img src="dashboard/dashboard_preview.png" width="1000">
</p>

---

# 📋 Key Project Deliverables

✅ Enterprise Data Warehouse

✅ ETL Pipeline Development

✅ Exploratory Data Analysis

✅ Customer Analytics

✅ Customer Lifetime Value Analysis

✅ Customer Segmentation

✅ Customer Churn Prediction

✅ Sales Forecasting

✅ Cohort Retention Analysis

✅ Interactive Power BI Dashboard
