INSERT INTO student (name, study_group_id) VALUES (?, ?);

INSERT INTO study_group (group_name) VALUES (?);

INSERT INTO teacher (name, is_sciens_title) VALUES (?, ?);

INSERT INTO stady_subject (subject_name, teacher_id) VALUES (?, ?);

INSERT INTO evaluation (student_id, subject_id,	evalution_val, created_at) VALUES (?, ?, ?, ?);