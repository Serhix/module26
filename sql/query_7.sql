SELECT e.evalution_val, s.name, sg.group_name, ss.subject_name 
FROM evaluation e 
JOIN stady_subject ss ON ss.id = e.subject_id 
JOIN student s ON s.id = e.student_id 
JOIN study_group sg ON sg.id = s.study_group_id
WHERE sg.id = 1 AND ss.id = 4;