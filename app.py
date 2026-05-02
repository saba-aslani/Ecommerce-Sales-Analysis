import streamlit as st
import sqlite3
import pandas as pd

conn = sqlite3.connect("ecommerce.db")

st.title("📊 E-commerce Sales Dashboard")

# Revenue
st.header("Revenue Trend")
query = """
SELECT 
    strftime('%Y-%m', invoicedate) AS month,
    SUM(revenue) AS revenue
FROM orders
GROUP BY month
ORDER BY month
"""
df = pd.read_sql(query, conn)
st.line_chart(df.set_index("month"))

# Top Products
st.header("Top Products")
query = """
SELECT description, SUM(revenue) AS revenue
FROM orders
GROUP BY description
ORDER BY revenue DESC
LIMIT 10
"""
df = pd.read_sql(query, conn)
st.bar_chart(df.set_index("description"))

# Top Customers
st.header("Top Customers")
query = """
SELECT customerid, SUM(revenue) AS revenue
FROM orders
GROUP BY customerid
ORDER BY revenue DESC
LIMIT 10
"""
df = pd.read_sql(query, conn)
st.bar_chart(df.set_index("customerid"))