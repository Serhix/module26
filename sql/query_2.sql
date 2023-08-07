SELECT s.name, ROUND(AVG(e.evalution_val), 2) AS avg_score
FROM student s
JOIN evaluation e ON s.id = e.student_id
WHERE e.subject_id = 6
GROUP BY s.name
ORDER BY avg_score DESC
LIMIT 1 ;