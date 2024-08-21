# Write your MySQL query statement below
WITH FirstYearSales AS (
    SELECT product_id,
           MIN(year) as first_year_order
    FROM Sales
    GROUP BY product_id
)

SELECT s.product_id,
       s.year AS first_year,
       s.quantity,
       s.price
FROM Sales s
INNER JOIN FirstYearSales f
ON s.product_id = f.product_id AND
   s.year = f.first_year_order;
    