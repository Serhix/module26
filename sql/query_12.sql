SELECT e.evalution_val, sg.group_name, ss.subject_name, e.created_at 
FROM student s
JOIN evaluation e ON s.id = e.student_id
JOIN stady_subject ss ON e.subject_id = ss.id
JOIN study_group sg ON sg.id = s.study_group_id 
WHERE sg.id = 1 
AND ss.id = 3 
AND e.created_at = (SELECT MAX(created_at) FROM evaluation);