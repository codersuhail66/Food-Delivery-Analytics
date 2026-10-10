
USE food_delivery_analytics;

-- 1. Total orders
SELECT COUNT(*) AS total_orders
FROM food_orders;

-- 2. Total net sales
SELECT ROUND(SUM(net_sales), 2) AS total_net_sales
FROM food_orders;

-- 3. Average order value
SELECT ROUND(AVG(order_value), 2) AS average_order_value
FROM food_orders;

-- 4. Average customer rating
SELECT ROUND(AVG(rating), 2) AS average_rating
FROM food_orders;

-- 5. Sales by month
SELECT
    month,
    month_number,
    ROUND(SUM(net_sales), 2) AS total_sales
FROM food_orders
GROUP BY month, month_number
ORDER BY month_number;

-- 6. Sales by state
SELECT
    state,
    ROUND(SUM(net_sales), 2) AS total_sales
FROM food_orders
GROUP BY state
ORDER BY total_sales DESC;

-- 7. Top 10 restaurants by sales
SELECT
    restaurant,
    ROUND(SUM(net_sales), 2) AS total_sales,
    COUNT(*) AS total_orders
FROM food_orders
GROUP BY restaurant
ORDER BY total_sales DESC
LIMIT 10;

-- 8. Orders by payment mode
SELECT
    payment_mode,
    COUNT(*) AS total_orders
FROM food_orders
GROUP BY payment_mode
ORDER BY total_orders DESC;

-- 9. Order status breakdown
SELECT
    order_status,
    COUNT(*) AS total_orders
FROM food_orders
GROUP BY order_status
ORDER BY total_orders DESC;

-- 10. Sales by food category
SELECT
    category,
    ROUND(SUM(net_sales), 2) AS total_sales,
    COUNT(*) AS total_orders
FROM food_orders
GROUP BY category
ORDER BY total_sales DESC;