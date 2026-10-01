import sqlite3
from pathlib import Path

conn = sqlite3.connect("Company_db")
# Use db_path so it connects to the database in the same directory
db_path = Path(__file__).parent / "Company_db"

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS employees (
        emp_id INT PRIMARY KEY,
        emp_name VARCHAR(50),
        dep_id INT,
        salary INT
        )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS department(
    dept_id INT,
    dept_name VARCHAR(50),
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(50)
    )
""")

employees_data = [
    (1, "Alice", 101, 50000),
    (2, "Bob", 102, 70000),
    (3, "Charlie", 102, 65000),
    (4, "David", 103, 55000),
    (5, "Eve", None, 45000),
    (6, "Frank", 102, 60000)  
]

cursor.executemany("""
    INSERT OR IGNORE INTO employees (emp_id, emp_name, dep_id, salary)
    VALUES (?, ?, ?, ?)
""", employees_data)


department_data = [
    (101, "HR"),
    (102, "IT"),
    (103, "Finance"),
    (104, "Marketing")
]

cursor.executemany("""
    INSERT OR IGNORE INTO department (dept_id, dept_name)
    VALUES (?, ?)
""", department_data)

conn.commit()

# Tasks

# 1. Display Employee name with Department 
print("1. Employee name with Department:")
cursor.execute("""
    SELECT employees.emp_name, department.dept_name
    FROM employees
    INNER JOIN department ON employees.dep_id = department.dept_id
""")
for emp_name, dept_name in cursor.fetchall():
    print(f"Employee: {emp_name} -> Department: {dept_name}")
print()


# 2. Display Employees earning more than 50000
print("2. Employees earning more than 50000:")
cursor.execute("""
    SELECT employees.emp_name, department.dept_name, employees.salary
    FROM employees
    LEFT JOIN department ON employees.dep_id = department.dept_id
    WHERE employees.salary > 50000
""")
for emp_name, dept_name, salary in cursor.fetchall():
    dept = dept_name if dept_name else "No Department"
    print(f"Employee: {emp_name} | Department: {dept} | Salary: {salary}")
print()


# 3. Display department-wise total salary
print("3. Department-wise total salary:")
cursor.execute("""
    SELECT department.dept_name, SUM(employees.salary) AS total_salary
    FROM department
    INNER JOIN employees ON department.dept_id = employees.dep_id
    GROUP BY department.dept_name
""")
for dept_name, total_salary in cursor.fetchall():
    print(f"Department: {dept_name} -> Total Salary: {total_salary}")
print()


# 4. Display Department with more than 2 employees
print("4. Department with more than 2 employees:")
cursor.execute("""
    SELECT department.dept_name, COUNT(employees.emp_id) AS emp_count
    FROM department
    INNER JOIN employees ON department.dept_id = employees.dep_id
    GROUP BY department.dept_name
    HAVING COUNT(employees.emp_id) > 2
""")
for dept_name, emp_count in cursor.fetchall():
    print(f"Department: {dept_name} -> Employees: {emp_count}")
print()


# 5. Display employees without a department
print("5. Employees without a department:")
cursor.execute("""
    SELECT employees.emp_name, employees.salary
    FROM employees
    LEFT JOIN department ON employees.dep_id = department.dept_id
    WHERE department.dept_id IS NULL
""")
for emp_name, salary in cursor.fetchall():
    print(f"Employee: {emp_name} (Salary: {salary})")
print()

conn.close()