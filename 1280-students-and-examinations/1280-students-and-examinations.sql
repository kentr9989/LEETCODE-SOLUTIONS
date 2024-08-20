# Write your MySQL query statement below
SELECT stu.student_id AS student_id,
       stu.student_name AS student_name,
       sub.subject_name AS subject_name,
       COUNT(exa.subject_name) AS attended_exams
FROM Students stu
CROSS JOIN Subjects sub
LEFT JOIN Examinations exa 
ON sub.subject_name = exa.subject_name AND
   stu.student_id = exa.student_id
GROUP BY stu.student_id, stu.student_name, sub.subject_name
ORDER BY stu.student_id, sub.subject_name;