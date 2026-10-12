
import sqlite3
from pathlib import Path

# Create a separate database
db_path = Path(__file__).parent / "EmployeeQueries.db"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Create employees table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS employees (
        employee_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        salary REAL NOT NULL,
        hire_date TEXT NOT NULL,
        department TEXT
    )
""")

# Create a table to demonstrate common records
cursor.execute("""
    CREATE TABLE IF NOT EXISTS employee_archive (
        employee_id INTEGER,
        name TEXT,
        salary REAL
    )
""")

# Sample employees
cursor.executemany("""
    INSERT OR IGNORE INTO employees
        (employee_id, name, salary, hire_date, department)
    VALUES (?, ?, ?, ?, ?)
""", [
    (1, "Amit", 50000, "2025-01-10", "IT"),
    (2, "Priya", 70000, "2026-08-15", "HR"),
    (3, "Rahul", 60000, "2026-07-20", "IT"),
    (4, "Neha", 70000, "2025-11-05", "Finance"),
    (5, "Karan", 40000, "2026-09-01", "IT"),
    (6, "Amit", 50000, "2025-01-10", "IT")
])

# Sample archive records
cursor.executemany("""
    INSERT INTO employee_archive
        (employee_id, name, salary)
    VALUES (?, ?, ?)
""", [
    (1, "Amit", 50000),
    (3, "Rahul", 60000),
    (7, "Meera", 45000)
])

conn.commit()


# 1. Find the Nth highest DISTINCT salary
print("\n1. Nth Highest Salary")

N = 2  # Change this to 1, 2, 3, etc.

cursor.execute("""
    SELECT DISTINCT salary
    FROM employees
    ORDER BY salary DESC
    LIMIT 1 OFFSET ?
""", (N - 1,))

result = cursor.fetchone()

if result:
    print(f"{N}th highest salary:", result[0])
else:
    print("Salary rank does not exist.")


# 2. Remove duplicate records
print("\n2. Remove Duplicate Records")

# Keep the smallest employee_id for each identical
# name, salary, hire_date and department combination.
cursor.execute("""
    DELETE FROM employees
    WHERE employee_id NOT IN (
        SELECT MIN(employee_id)
        FROM employees
        GROUP BY name, salary, hire_date, department
    )
""")

print("Duplicate employee records removed.")
conn.commit()


# 3. Find records common in two tables
print("\n3. Common Records in Both Tables")

cursor.execute("""
    SELECT e.employee_id, e.name, e.salary
    FROM employees e
    INNER JOIN employee_archive a
        ON e.employee_id = a.employee_id
       AND e.name = a.name
       AND e.salary = a.salary
""")

for row in cursor.fetchall():
    print(row)


# 4. Find employees hired in the last 6 months
print("\n4. Employees Hired in the Last 6 Months")

cursor.execute("""
    SELECT employee_id, name, hire_date
    FROM employees
    WHERE hire_date >= date('now', '-6 months')
      AND hire_date <= date('now')
    ORDER BY hire_date DESC
""")

for row in cursor.fetchall():
    print(row)


# 5. Find consecutive duplicate salary values
print("\n5. Consecutive Duplicate Salary Values")

cursor.execute("""
    WITH ordered_employees AS (
        SELECT
            employee_id,
            name,
            salary,
            LAG(salary) OVER (
                ORDER BY employee_id
            ) AS previous_salary
        FROM employees
    )
    SELECT employee_id, name, salary
    FROM ordered_employees
    WHERE salary = previous_salary
""")

for row in cursor.fetchall():
    print(row)


conn.close()