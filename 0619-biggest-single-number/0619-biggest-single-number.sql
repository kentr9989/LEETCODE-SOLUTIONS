# Write your MySQL query statement below
WITH SingleNumberTable AS (
    SELECT num as single_num
    FROM MyNumbers
    GROUP BY num
    HAVING COUNT(num) = 1
)

SELECT MAX(single_num) as num
FROM SingleNumberTable;