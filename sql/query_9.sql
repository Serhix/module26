SELECT ss.subject_name, s.name 
FROM evaluation e 
JOIN student s ON s.id = e.student_id 
JOIN stady_subject ss ON ss.id = e.subject_id 
WHERE s.id = 18
GROUP BY ss.subject_name ;