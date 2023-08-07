SELECT s.name, ROUND(AVG(e.evalution_val), 2) AS avg_score
FROM student s
LEFT JOIN evaluation e ON s.id = e.student_id
GROUP BY s.name
ORDER BY avg_score DESC
LIMIT 5;