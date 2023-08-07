SELECT s.name as student_list, sg.group_name
FROM student s 
JOIN study_group sg ON sg.id = s.study_group_id
WHERE sg.id = 1;