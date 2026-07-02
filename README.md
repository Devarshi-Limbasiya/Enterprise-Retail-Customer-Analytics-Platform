# 📊 Enterprise Retail Customer Analytics Platform

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

The **Enterprise Retail Customer Analytics Platform** is an enterprise-grade customer analytics and business intelligence solution developed using **SQL Server, Python, Machine Learning, and Power BI**.

This project integrates **Data Engineering, Data Analytics, Machine Learning, and Business Intelligence** to transform raw retail transaction data into actionable business insights for strategic decision-making.

The platform enables organizations to:

- Understand customer purchasing behavior
- Segment customers intelligently
- Predict customer churn
- Estimate customer lifetime value
- Analyze customer retention
- Forecast future sales revenue
- Visualize business KPIs through executive dashboards

---

# 🚀 Business Objectives

This project addresses several critical business challenges:

✅ Identify high-value customers

✅ Segment customers based on purchasing behavior

✅ Predict customer churn risk

✅ Forecast future sales revenue

✅ Analyze customer retention patterns

✅ Calculate customer lifetime value

✅ Develop executive business dashboards

✅ Build an enterprise-scale customer analytics ecosystem

---

# ⭐ Project Highlights

✔ Designed and implemented an Enterprise Data Warehouse using SQL Server

✔ Developed ETL pipelines using Bronze → Silver → Gold architecture

✔ Performed Exploratory Data Analysis using Python

✔ Built Customer RFM Analytics framework

✔ Developed Customer Lifetime Value (CLV) analysis

✔ Implemented Customer Cohort Retention Analysis

✔ Developed Customer Segmentation using K-Means Clustering

✔ Built Customer Churn Prediction models

✔ Created Sales Forecasting models

✔ Developed interactive Power BI dashboards

---

# 🏗️ System Architecture

<p align="center">
  <img src="architecture/enterprise_retail_architecture.png" width="1000">
</p>

The architecture follows a layered enterprise analytics approach:

```text
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

# 🔄 Project Workflow

<p align="center">
  <img src="architecture/analytics_workflow.png" width="1000">
</p>

The project workflow follows these stages:

```text
CRM + ERP Data
       ↓
ETL Pipelines
       ↓
SQL Server Data Warehouse
(Bronze → Silver → Gold)
       ↓
Master Dataset Creation
       ↓
Exploratory Data Analysis
       ↓
Customer Analytics
(RFM, CLV, Cohort)
       ↓
Machine Learning
(Segmentation, Churn, Forecasting)
       ↓
Power BI Dashboard
       ↓
Business Insights
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

# 📊 Project Statistics

| Metric | Value |
|---------|---------|
| Customers | 18,000+ |
| Transactions | 50,000+ |
| Countries | 6 |
| Data Warehouse Layers | 3 |
| Machine Learning Models | 3 |
| Analytical Modules | 5 |
| Visualizations | 12+ |
| SQL Scripts | 14 |
| Power BI Dashboards | 1 |

---

# 📈 Business KPIs Generated

- Total Revenue
- Total Customers
- Average Order Value
- Customer Lifetime Value
- Customer Retention Rate
- Customer Churn Rate
- Customer Segmentation
- Sales Growth Rate
- Forecasted Revenue
- Geographic Revenue Distribution

---

# 🗄️ Data Warehouse Architecture

The project follows a multi-layer enterprise warehouse design.

### Bronze Layer
Raw CRM and ERP datasets.

### Silver Layer
Cleaned, validated, standardized and transformed datasets.

### Gold Layer
Business-ready analytical datasets and reporting tables.

---

## Star Schema Design

### Fact Table

- fact_sales

### Dimension Tables

- dim_customers
- dim_products
- dim_dates

---

# 📈 Exploratory Data Analysis

Exploratory analysis was performed to identify trends, customer behavior patterns, and revenue insights.

## Annual Sales Revenue

<p align="center">
<img src="outputs/eda/sales_by_year.png" width="700">
</p>

---

## Top Countries by Sales Revenue

<p align="center">
<img src="outputs/eda/top_countries.png" width="700">
</p>

---

# 👥 Customer RFM Analysis

RFM analysis was performed to understand customer purchasing behavior using:

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
<img src="outputs/analytics/rfm_frequency_monetary.png" width="700">
</p>

---

## Customer Segments

<p align="center">
<img src="outputs/analytics/customer_segments.png" width="700">
</p>

---

# 💰 Customer Lifetime Value Analysis

Customer Lifetime Value (CLV) analysis was conducted to identify long-term customer profitability.

## CLV Distribution

<p align="center">
<img src="outputs/analytics/clv_distribution.png" width="700">
</p>

---

## Top Customers by CLV

<p align="center">
<img src="outputs/analytics/top_customers_clv.png" width="700">
</p>

---

# 🔄 Customer Cohort Retention Analysis

Cohort analysis was performed to analyze customer retention and repeat purchasing behavior.

<p align="center">
<img src="outputs/analytics/cohort_retention_analysis.png" width="1000">
</p>

---

# 🧠 Customer Segmentation

K-Means clustering was applied to segment customers according to purchasing behavior.

<p align="center">
<img src="outputs/machine_learning/customer_segmentation_clusters.png" width="850">
</p>

---

# ⚠️ Customer Churn Prediction

A machine learning model was developed to predict customer churn behavior.

<p align="center">
<img src="outputs/machine_learning/customer_churn_feature_importance.png" width="700">
</p>

---

# 📈 Sales Forecasting

Historical sales data was analyzed to forecast future revenue trends.

## Monthly Sales Revenue Trend

<p align="center">
<img src="outputs/machine_learning/monthly_sales_trend.png" width="800">
</p>

---

## Historical vs Forecasted Sales Revenue

<p align="center">
<img src="outputs/machine_learning/sales_forecasting_prediction.png" width="1000">
</p>

---

# 💡 Key Business Insights

- United States and Australia generated the highest sales revenue.
- Customer Recency emerged as the strongest indicator of customer churn.
- Loyal customers contribute a significant portion of total revenue.
- High-frequency customers exhibit substantially higher lifetime value.
- Customer retention decreases considerably after initial purchase periods.
- Sales revenue demonstrates a positive long-term growth trend.
- Customer segmentation reveals distinct purchasing behavior patterns.

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

✅ Enterprise Data Warehouse Development

✅ ETL Pipeline Development

✅ Exploratory Data Analysis

✅ Customer RFM Analysis

✅ Customer Lifetime Value Analysis

✅ Customer Cohort Retention Analysis

✅ Customer Segmentation using K-Means

✅ Customer Churn Prediction

✅ Sales Forecasting

✅ Executive Power BI Dashboard

✅ Enterprise Customer Analytics Platform
