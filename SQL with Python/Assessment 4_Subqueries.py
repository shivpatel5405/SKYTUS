import sqlite3
from pathlib import Path

db_path = Path(__file__).parent / "College.db"

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# 1. Employees earning more than average salary
print("1. Employees earning more than average salary:")

cursor.execute("""
    SELECT *
    FROM employees
    WHERE salary > (
        SELECT AVG(salary)
        FROM employees
    )
""")

for employee in cursor.fetchall():
    print(employee)


# 2. Department with highest total salary
print("\n2. Department with highest total salary:")

cursor.execute("""
    SELECT department, SUM(salary) AS total_salary
    FROM employees
    GROUP BY department
    ORDER BY total_salary DESC
    LIMIT 1
""")

result = cursor.fetchone()
print(result)


# 3. Employee with second highest salary
print("\n3. Employee with second highest salary:")

cursor.execute("""
    SELECT *
    FROM employees
    ORDER BY salary DESC
    LIMIT 1 OFFSET 1
""")

result = cursor.fetchone()
print(result)


# 4. Employees working in the same department as Amit
print("\n4. Employees working in the same department as Amit:")

cursor.execute("""
    SELECT *
    FROM employees
    WHERE department = (
        SELECT department
        FROM employees
        WHERE name = 'Amit'
    )
""")

for employee in cursor.fetchall():
    print(employee)
