import sqlite3

conn = sqlite3.connect("College.db")
print(f"Database created successfully")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        student_id INT PRIMARY KEY,
        name VARCHAR(50),
        department VARCHAR(30),
        year INT,
        marks INT
    )
""")
students_data = [
    (1, "Rahul", "CSE", 3, 85),
    (2, "Amit", "IT", 2, 72),
    (3, "Priya", "CSE", 4, 91),
    (4, "Neha", "ECE", 3, 68),
    (5, "Rohan", "CSE", 2, 78)
]

cursor.executemany("""
    INSERT OR IGNORE INTO students
    (student_id, name, department, year, marks)
    VALUES (?, ?, ?, ?, ?)
""", students_data)

conn.commit()

# TASK 
# 1. Display all student records
cursor.execute("SELECT * FROM Students")

students_data = cursor.fetchall()

for student in students_data:
    print(student)


# 2. Display only name and department
print("\nDisplay only name and department")
cursor.execute("SELECT name , department FROM Students")
students_data = cursor.fetchall()
for student in students_data:
    print(student)


# 3. Find students with marks greater than 75
print("\nFind students with marks greater than 75")
cursor.execute("SELECT * FROM Students WHERE marks>75")
students_data = cursor.fetchall()
for student in students_data:
    print(student)


# 4. Display students from CSE department
print("\nDisplay students from CSE department")
cursor.execute("SELECT * FROM Students WHERE department = 'CSE'")

students_data = cursor.fetchall()
for student in students_data:
    print(student)


# 5. Sort students by marks — descending
print("\nSort students by marks — descending")
cursor.execute("SELECT * FROM Students ORDER BY marks DESC")

students_data = cursor.fetchall()
for student in students_data:
    print(student)


# 6. Display top 3 scorers
print("\nDisplay top 3 scorers")
cursor.execute(""" 
    SELECT * FROM Students 
    ORDER BY marks DESC 
    LIMIT 3
""")

students_data = cursor.fetchall()
for student in students_data:
    print(student)