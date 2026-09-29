import sqlite3
from pathlib import Path

# Use db_path so it works regardless of working directory
db_path = Path(__file__).parent / "College.db"

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

#Tasks
# 1. Total number of students
print("1. Total number of students:")
cursor.execute("SELECT COUNT(*) FROM students")
total_students = cursor.fetchone()[0]
print(f"Total students: {total_students}\n")


# 2. Average marks of all students
print("2. Average marks:")
cursor.execute("SELECT ROUND(AVG(marks), 2) FROM students")
avg_marks = cursor.fetchone()[0]
print(f"Average marks: {avg_marks}\n")


# 3. Highest and lowest marks
print("3. Highest and Lowest marks:")
cursor.execute("SELECT MAX(marks), MIN(marks) FROM students")
max_marks, min_marks = cursor.fetchone()
print(f"Highest Marks: {max_marks}, Lowest Marks: {min_marks}\n")


# 4. Department wise average marks
print("4. Department wise average marks:")
cursor.execute("""
    SELECT department, ROUND(AVG(marks), 2)
    FROM students
    GROUP BY department
""")
for dept, avg_marks in cursor.fetchall():
    print(f"Department: {dept} -> Average Marks: {avg_marks}")
print()


# 5. Display Department where average marks > 70
print("5. Department where average marks > 70:")
cursor.execute("""
    SELECT department, ROUND(AVG(marks), 2)
    FROM students
    GROUP BY department
    HAVING AVG(marks) > 70
""")
for dept, avg_marks in cursor.fetchall():
    print(f"Department: {dept} -> Average Marks: {avg_marks}")
print()

conn.close()
