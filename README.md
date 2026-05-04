# 📊 E-commerce Sales Analysis

## Overview
This project performs an end-to-end analysis of e-commerce sales data using Python, SQL, and data visualization techniques.

The goal is to transform raw transactional data into actionable business insights.

---

## Key Features

- Data cleaning and preprocessing using Pandas
- Revenue analysis and trend visualization
- Customer segmentation (New vs Repeat)
- Top products and customer analysis
- Advanced SQL analysis (CTE, Window Functions, Subqueries)
- Interactive dashboard using Streamlit

---

## Advanced SQL Analysis

This project includes advanced SQL techniques:

- Window Functions (Customer Ranking)
- Subqueries (High-value transactions)
- CTE (Monthly revenue trend)

---

## Key Insights

- Revenue is concentrated among a small number of customers
- A limited set of products drives the majority of revenue
- Sales show seasonal trends with peak periods
- High-value transactions play a major role in business performance

---

## Tech Stack
- Python (pandas, matplotlib)
- SQL (SQLite)
- Jupyter Notebook
- Streamlit (for dashboard)
- Git & GitHub

---

## 📂 Project Structure

```
Ecommerce-Sales-Analysis/
│
├── data/
│   └── online_retail.csv
│
├── notebook/
│   └── analysis.ipynb
│
├── sql/
│   └── queries.sql
│
├── app.py
├── ecommerce.db
├── images
├── requirements.txt
└── README.md
```

---

## Data Preparation

- Standardized column names
- Converted invoice dates to datetime
- Removed missing customer IDs
- Removed invalid (negative/zero) transactions
- Created revenue feature

---

## SQL Analysis
This project emphasizes **SQL-driven analytics**, including:

- Aggregations (GROUP BY, SUM)
- Subqueries (high-value transactions)
- Window Functions (customer ranking)

- CTE (monthly revenue trends)

---

## Key Insights

- Revenue is highly concentrated among a small number of customers
- A limited set of products drives most of the sales (Pareto effect)
- Monthly revenue shows growth with seasonal patterns
- High-value transactions significantly impact overall performance
- Repeat customers are critical for long-term business sustainability

---

## 💡 Business Recommendations

- Focus on retaining high-value customers
- Prioritize top-performing products in marketing and inventory
- Leverage seasonal trends for campaign planning
- Develop strategies for increasing repeat customer rate

---

## 📊 Dashboard

An interactive dashboard built with Streamlit visualizes:
- Revenue trends over time
- Top products
- Top customers
- Customer behavior (new vs repeat)
- High-value transactions

### Run the dashboard
```bash
streamlit run app.py
```
## Dashboard Preview
![Dashboard](images/dashboard.png)

---

## How to Run the Project
### 1. Install dependencies
```bash
pip install -r requirements.txt
```
### 2. Open the notebook
```bash
jupyter notebook
```
### 3. Run the dashboard
```bash
streamlit run app.py
```

---

## Project Highlights
- Built a SQL-heavy business analytics project
- Created an interactive Streamlit dashboard
- Used SQL queries to answer real business questions
- Analyzed revenue, products, customers, and retention
- Turned raw transaction data into actionable insights

---

## Author
### Saba Aslani
Data Analyst / Data Engineer
