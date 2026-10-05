SELECT t.name
FROM teachers t
LEFT JOIN departments d
ON t.dept_id = d.dept_id
WHERE d.dept_id IS NULL;