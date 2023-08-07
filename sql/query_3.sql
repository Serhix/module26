SELECT ss.subject_name, sg.group_name, ROUND(AVG(e.evalution_val), 2) AS avg_score
FROM evaluation e
JOIN student s ON s.id = e.student_id 
JOIN study_group sg ON sg.id = s.study_group_id 
JOIN stady_subject ss ON ss.id = e.subject_id 
WHERE ss.id = 3
GROUP BY sg.group_name, ss.subject_name 
ORDER BY avg_score DESC;