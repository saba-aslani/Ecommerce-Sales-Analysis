import sqlite3
import pandas as pd
import streamlit as st


# Page configuration
st.set_page_config(
    page_title="E-commerce Sales Dashboard",
    layout="wide"
)


# App title
st.title("📊 E-commerce Sales Analysis Dashboard")

st.markdown(
    """
    This dashboard presents key business insights from e-commerce transaction data
    using SQL-based analysis.
    """
)


# Connect to SQLite database
conn = sqlite3.connect("ecommerce.db")


# Monthly revenue trend
st.header("📈 Monthly Revenue Trend")

monthly_revenue_query = """
SELECT 
    strftime('%Y-%m', invoicedate) AS month,
    ROUND(SUM(revenue), 2) AS total_revenue
FROM orders
GROUP BY month
ORDER BY month;
"""

monthly_revenue = pd.read_sql(monthly_revenue_query, conn)

st.line_chart(monthly_revenue.set_index("month"))


# Top products by revenue
st.header("🛍️ Top Products by Revenue")

top_products_query = """
SELECT 
    description,
    ROUND(SUM(revenue), 2) AS total_revenue,
    SUM(quantity) AS total_quantity
FROM orders
GROUP BY description
ORDER BY total_revenue DESC
LIMIT 10;
"""

top_products = pd.read_sql(top_products_query, conn)

st.bar_chart(top_products.set_index("description")["total_revenue"])
st.dataframe(top_products)


# Top customers with ranking
st.header("👥 Top Customers by Revenue")

top_customers_query = """
SELECT 
    customerid,
    ROUND(SUM(revenue), 2) AS total_revenue,
    COUNT(DISTINCT invoiceno) AS total_orders,
    RANK() OVER (ORDER BY SUM(revenue) DESC) AS customer_rank
FROM orders
GROUP BY customerid
ORDER BY total_revenue DESC
LIMIT 10;
"""

top_customers = pd.read_sql(top_customers_query, conn)

st.dataframe(top_customers)


# High-value transactions
st.header("💰 High-Value Transactions")

high_value_query = """
SELECT 
    invoiceno,
    stockcode,
    description,
    customerid,
    country,
    quantity,
    unitprice,
    ROUND(revenue, 2) AS revenue
FROM orders
WHERE revenue > (
    SELECT AVG(revenue)
    FROM orders
)
ORDER BY revenue DESC
LIMIT 20;
"""

high_value_orders = pd.read_sql(high_value_query, conn)

st.dataframe(high_value_orders)


# Repeat vs New customers
st.header("🔁 New vs Repeat Customers")

repeat_query = """
SELECT 
    customer_type,
    COUNT(*) AS customer_count
FROM (
    SELECT 
        customerid,
        CASE 
            WHEN COUNT(DISTINCT invoiceno) > 1 THEN 'Repeat'
            ELSE 'New'
        END AS customer_type
    FROM orders
    GROUP BY customerid
)
GROUP BY customer_type;
"""

repeat_customers = pd.read_sql(repeat_query, conn)

st.bar_chart(repeat_customers.set_index("customer_type"))


# Close database connection
conn.close()