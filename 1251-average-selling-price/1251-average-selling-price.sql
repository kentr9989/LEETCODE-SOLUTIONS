# Write your MySQL query statement below
# SELECT p.product_id,
#        ROUND(SUM(p.price * u.units)/ SUM(u.units),2) AS average_price
# FROM Prices p
# INNER JOIN UnitsSold u 
# ON p.product_id = u.product_id AND
#    u.purchase_date BETWEEN p.start_date AND p.end_date
# GROUP BY u.product_id;

select p.product_id, ifnull(round(sum(p.price * u.units)/sum(u.units),2),0) as average_price
from prices as p left join unitsSold as u
on p.product_id = u.product_id and 
u.purchase_date between start_date and end_date
group by product_id;