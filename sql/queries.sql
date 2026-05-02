# SQL query: top countries by revenue
query = """
SELECT
    country,
    ROUND(SUM(revenue),2) AS total_revenue
FROM orders
GROUP BY country
ORDER BY total_revenue DESC
LIMIT 10
"""

# SQL query: top products by revenue
query = """
SELECT 
    description,
    ROUND(SUM(revenue), 2) AS total_revenue,
    SUM(quantity) AS total_quantity
FROM orders
GROUP BY description
ORDER BY total_revenue DESC
LIMIT 10
"""

# SQL query: top customers by revenue
query = """
SELECT 
    customerid,
    ROUND(SUM(revenue), 2) AS total_revenue,
    COUNT(DISTINCT invoiceno) AS total_orders
FROM orders
GROUP BY customerid
ORDER BY total_revenue DESC
LIMIT 10
"""

# SQL: classify customers based on number of orders
query = """
SELECT 
    customerid,
    COUNT(DISTINCT invoiceno) AS total_orders
FROM orders
GROUP BY customerid
"""