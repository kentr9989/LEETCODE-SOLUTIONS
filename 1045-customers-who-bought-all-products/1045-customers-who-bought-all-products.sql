# Write your MySQL query statement below
WITH CustomerBuyAll AS (
    SELECT customer_id,
           COUNT(DISTINCT product_key) AS count
    FROM Customer
    GROUP BY customer_id
)

SELECT customer_id
FROM CustomerBuyAll
WHERE count = (SELECT COUNT(DISTINCT product_key) FROM Product);