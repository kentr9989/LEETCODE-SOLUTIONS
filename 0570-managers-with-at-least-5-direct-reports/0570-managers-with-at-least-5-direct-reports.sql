# Write your MySQL query statement below
SELECT e1.name 
FROM Employee e1 
JOIN (
    SELECT *,COUNT(e2.managerId)
    FROM Employee e2
    WHERE e2.managerId IS NOT NULL
    GROUP BY e2.managerId
    HAVING COUNT(e2.id) >= 5
) e2 ON e1.id = e2.managerId
