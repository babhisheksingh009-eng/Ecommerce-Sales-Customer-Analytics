
-- 1. Total Revenue
SELECT ROUND(SUM(Revenue), 2) AS total_revenue
FROM online_retail;

-- 2. Monthly Sales
SELECT
    DATE_FORMAT(InvoiceDate, '%Y-%m') AS sales_month,
    ROUND(SUM(Revenue), 2) AS monthly_revenue
FROM online_retail
GROUP BY DATE_FORMAT(InvoiceDate, '%Y-%m')
ORDER BY sales_month;

-- 3. Top 10 Customers
SELECT
    CustomerID,
    ROUND(SUM(Revenue), 2) AS total_spent,
    COUNT(DISTINCT InvoiceNo) AS total_orders
FROM online_retail
WHERE CustomerID IS NOT NULL
GROUP BY CustomerID
ORDER BY total_spent DESC
LIMIT 10;

-- 4. Repeat Customer Percentage
SELECT
    ROUND(100.0 * SUM(order_count > 1) / COUNT(*), 2)
        AS repeat_customer_percentage
FROM (
    SELECT
        CustomerID,
        COUNT(DISTINCT InvoiceNo) AS order_count
    FROM online_retail
    WHERE CustomerID IS NOT NULL
    GROUP BY CustomerID
) AS customer_summary;

-- 5. Top 10 Best-Selling Products
SELECT
    Description,
    SUM(Quantity) AS total_quantity_sold,
    ROUND(SUM(Revenue), 2) AS total_revenue
FROM online_retail
GROUP BY Description
ORDER BY total_quantity_sold DESC
LIMIT 10;

-- 6. Top 10 Countries by Revenue
SELECT
    Country,
    ROUND(SUM(Revenue), 2) AS total_revenue,
    SUM(Quantity) AS total_quantity_sold
FROM online_retail
GROUP BY Country
ORDER BY total_revenue DESC
LIMIT 10;
