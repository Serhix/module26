SELECT ss.subject_name, t.name  
FROM stady_subject ss 
JOIN teacher t ON t.id = ss.teacher_id 
WHERE t.id = 2;
