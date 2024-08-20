# Write your MySQL query statement below
SELECT c.id,
       c.movie,
       c.description,
       c.rating
FROM Cinema c
WHERE MOD(c.id,2) = 1 AND description <> "boring"
ORDER BY c.rating DESC;