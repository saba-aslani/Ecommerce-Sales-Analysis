-- =========================================================
-- E-commerce Sales Analysis - SQL Queries
-- Author: Saba Aslani
-- Purpose: Business analytics using SQLite
-- =========================================================


-- =========================================================
-- 1. Monthly Revenue Trend
-- Business Question:
-- How does revenue change over time?
-- =========================================================

SELECT
    strftime('%Y-%m', invoicedate) AS month,
    ROUND(SUM(revenue), 2) AS total_revenue
FROM orders
GROUP BY month
ORDER BY month;


-- =========================================================
-- 2. Top Countries by Revenue
-- Business Question:
-- Which countries generate the most revenue?
-- =========================================================

SELECT
    country,
    ROUND(SUM(revenue), 2) AS total_revenue
FROM orders
GROUP BY country
ORDER BY total_revenue DESC
LIMIT 10;


-- =========================================================
-- 3. Top Products by Revenue
-- Business Question:
-- Which products drive the most sales?
-- =========================================================

SELECT
    description,
    ROUND(SUM(revenue), 2) AS total_revenue,
    SUM(quantity) AS total_quantity
FROM orders
GROUP BY description
ORDER BY total_revenue DESC
LIMIT 10;


-- =========================================================
-- 4. Top Customers by Revenue
-- Business Question:
-- Who are the highest-value customers?
-- =========================================================

SELECT
    customerid,
    ROUND(SUM(revenue), 2) AS total_revenue,
    COUNT(DISTINCT invoiceno) AS total_orders
FROM orders
GROUP BY customerid
ORDER BY total_revenue DESC
LIMIT 10;


-- =========================================================
-- 5. Customer Ranking - Window Function
-- Business Question:
-- How do customers rank by revenue contribution?
-- =========================================================

SELECT
    customerid,
    ROUND(SUM(revenue), 2) AS total_revenue,
    RANK() OVER (ORDER BY SUM(revenue) DESC) AS customer_rank
FROM orders
GROUP BY customerid
LIMIT 10;


-- =========================================================
-- 6. High-Value Transactions - Subquery
-- Business Question:
-- Which transactions are above average revenue?
-- =========================================================

SELECT *
FROM orders
WHERE revenue > (
    SELECT AVG(revenue)
    FROM orders
)
LIMIT 10;


-- =========================================================
-- 7. Monthly Revenue Trend - CTE
-- Business Question:
-- Can we calculate monthly revenue using a reusable query block?
-- =========================================================

WITH monthly_revenue AS (
    SELECT
        strftime('%Y-%m', invoicedate) AS month,
        ROUND(SUM(revenue), 2) AS total_revenue
    FROM orders
    GROUP BY month
)
SELECT *
FROM monthly_revenue
ORDER BY month;