SELECT  ss.subject_name, ROUND(AVG(e.evalution_val), 2) AS avg_score, t.name 
FROM evaluation e  
JOIN stady_subject ss ON ss.id = e.subject_id 
JOIN teacher t ON t.id = ss.teacher_id 
WHERE t.id = 3
GROUP BY ss.subject_name;