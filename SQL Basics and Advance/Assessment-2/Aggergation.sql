SELECT dept_id, COUNT(*) AS total_teachers
FROM teachers
GROUP BY dept_id;