SELECT ROUND(AVG(e.evalution_val), 2) AS average_score,  s.name, t.name 
FROM evaluation e 
JOIN student s ON s.id = e.student_id 
JOIN stady_subject ss ON ss.id = e.subject_id 
JOIN teacher t ON t.id = ss.teacher_id 
WHERE s.id = 1 AND t.id = 3
GROUP BY s.name , t.name ;