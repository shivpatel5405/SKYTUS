SELECT c.title, t.name
FROM courses c
INNER JOIN teachers t
ON c.teacher_id = t.teacher_id;