-- Create VIEW for first order

WITH FirstOrders AS (
    SELECT customer_id,
           MIN(order_date) AS first_order_date 
    FROM Delivery
    GROUP BY customer_id
)

SELECT 
    ROUND(SUM(CASE WHEN d.customer_pref_delivery_date = d.order_date THEN 1 ELSE 0 END) * 100
    / COUNT(*),2)  
    AS immediate_percentage
FROM Delivery d
JOIN FirstOrders f
ON f.customer_id = d.customer_id AND 
   f.first_order_date = d.order_date;