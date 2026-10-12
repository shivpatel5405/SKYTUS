
import sqlite3
from pathlib import Path
from datetime import date, timedelta

# ==================================================
# DATABASE CONNECTION
# ==================================================

db_path = Path(__file__).parent / "MessManagement.db"
conn = sqlite3.connect(db_path)
conn.execute("PRAGMA foreign_keys = ON")
cursor = conn.cursor()

today = date.today()


# ==================================================
# 1. CREATE TABLES AND RELATIONSHIPS
# ==================================================

cursor.executescript("""
CREATE TABLE IF NOT EXISTS students (
    student_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    room_no TEXT
);

CREATE TABLE IF NOT EXISTS mess_plans (
    plan_id INTEGER PRIMARY KEY,
    plan_name TEXT NOT NULL UNIQUE,
    monthly_fee REAL NOT NULL CHECK(monthly_fee >= 0),
    meals_per_day INTEGER NOT NULL
        CHECK(meals_per_day > 0)
);

CREATE TABLE IF NOT EXISTS subscriptions (
    subscription_id INTEGER PRIMARY KEY,
    student_id INTEGER NOT NULL,
    plan_id INTEGER NOT NULL,
    start_date TEXT NOT NULL,
    end_date TEXT NOT NULL,
    status TEXT NOT NULL
        CHECK(status IN ('active', 'expired', 'cancelled')),
    FOREIGN KEY(student_id) REFERENCES students(student_id),
    FOREIGN KEY(plan_id) REFERENCES mess_plans(plan_id),
    CHECK(end_date >= start_date)
);

CREATE TABLE IF NOT EXISTS meals (
    meal_id INTEGER PRIMARY KEY,
    meal_date TEXT NOT NULL,
    meal_type TEXT NOT NULL
        CHECK(meal_type IN ('Breakfast', 'Lunch', 'Dinner')),
    menu TEXT NOT NULL,
    UNIQUE(meal_date, meal_type)
);

CREATE TABLE IF NOT EXISTS meal_attendance (
    attendance_id INTEGER PRIMARY KEY,
    student_id INTEGER NOT NULL,
    meal_id INTEGER NOT NULL,
    attended INTEGER NOT NULL DEFAULT 1
        CHECK(attended IN (0, 1)),
    UNIQUE(student_id, meal_id),
    FOREIGN KEY(student_id) REFERENCES students(student_id),
    FOREIGN KEY(meal_id) REFERENCES meals(meal_id)
);

CREATE TABLE IF NOT EXISTS payments (
    payment_id INTEGER PRIMARY KEY,
    subscription_id INTEGER NOT NULL,
    amount REAL NOT NULL CHECK(amount >= 0),
    payment_date TEXT NOT NULL,
    status TEXT NOT NULL
        CHECK(status IN ('paid', 'pending', 'failed')),
    FOREIGN KEY(subscription_id)
        REFERENCES subscriptions(subscription_id)
);

CREATE TABLE IF NOT EXISTS feedback (
    feedback_id INTEGER PRIMARY KEY,
    student_id INTEGER NOT NULL,
    meal_id INTEGER NOT NULL,
    rating INTEGER NOT NULL CHECK(rating BETWEEN 1 AND 5),
    comments TEXT,
    FOREIGN KEY(student_id) REFERENCES students(student_id),
    FOREIGN KEY(meal_id) REFERENCES meals(meal_id)
);
""")


# ==================================================
# 2. INSERT SAMPLE DATA
# ==================================================

cursor.executemany("""
    INSERT OR IGNORE INTO students
        (student_id, name, email, room_no)
    VALUES (?, ?, ?, ?)
""", [
    (1, "Amit", "amit@example.com", "A101"),
    (2, "Priya", "priya@example.com", "A102"),
    (3, "Rahul", "rahul@example.com", "B201"),
    (4, "Neha", "neha@example.com", "B202"),
    (5, "Karan", "karan@example.com", "C301"),
    (6, "Meera", "meera@example.com", "C302")
])

cursor.executemany("""
    INSERT OR IGNORE INTO mess_plans
        (plan_id, plan_name, monthly_fee, meals_per_day)
    VALUES (?, ?, ?, ?)
""", [
    (1, "Basic", 3000, 2),
    (2, "Standard", 4500, 3),
    (3, "Premium", 6000, 3)
])

# Dates relative to today so active-subscription and
# recent-attendance queries work whenever you run the file.
cursor.executemany("""
    INSERT OR IGNORE INTO subscriptions
        (subscription_id, student_id, plan_id,
         start_date, end_date, status)
    VALUES (?, ?, ?, ?, ?, ?)
""", [
    (101, 1, 2, (today - timedelta(days=10)).isoformat(),
     (today + timedelta(days=20)).isoformat(), "active"),
    (102, 2, 3, (today - timedelta(days=5)).isoformat(),
     (today + timedelta(days=25)).isoformat(), "active"),
    (103, 3, 1, (today - timedelta(days=60)).isoformat(),
     (today - timedelta(days=30)).isoformat(), "expired"),
    (104, 4, 2, (today - timedelta(days=2)).isoformat(),
     (today + timedelta(days=28)).isoformat(), "active"),
    (105, 5, 1, (today - timedelta(days=15)).isoformat(),
     (today + timedelta(days=15)).isoformat(), "active")
])

cursor.executemany("""
    INSERT OR IGNORE INTO meals
        (meal_id, meal_date, meal_type, menu)
    VALUES (?, ?, ?, ?)
""", [
    (201, (today - timedelta(days=2)).isoformat(),
     "Breakfast", "Poha and tea"),
    (202, (today - timedelta(days=2)).isoformat(),
     "Lunch", "Dal, rice and roti"),
    (203, (today - timedelta(days=1)).isoformat(),
     "Breakfast", "Idli and sambar"),
    (204, (today - timedelta(days=1)).isoformat(),
     "Lunch", "Paneer, rice and roti"),
    (205, today.isoformat(),
     "Breakfast", "Upma and tea"),
    (206, today.isoformat(),
     "Lunch", "Rajma and rice"),
    (207, today.isoformat(),
     "Dinner", "Vegetable pulao")
])

cursor.executemany("""
    INSERT OR IGNORE INTO meal_attendance
        (attendance_id, student_id, meal_id, attended)
    VALUES (?, ?, ?, ?)
""", [
    (301, 1, 201, 1),
    (302, 1, 202, 1),
    (303, 1, 203, 1),
    (304, 1, 204, 1),
    (305, 1, 205, 1),
    (306, 2, 201, 1),
    (307, 2, 202, 1),
    (308, 2, 206, 1),
    (309, 3, 201, 1),
    (310, 4, 205, 1),
    (311, 4, 206, 1),
    (312, 5, 202, 1)
])

cursor.executemany("""
    INSERT OR IGNORE INTO payments
        (payment_id, subscription_id, amount,
         payment_date, status)
    VALUES (?, ?, ?, ?, ?)
""", [
    (401, 101, 4500, (today - timedelta(days=10)).isoformat(), "paid"),
    (402, 102, 6000, (today - timedelta(days=5)).isoformat(), "paid"),
    (403, 103, 3000, (today - timedelta(days=60)).isoformat(), "paid"),
    (404, 104, 4500, (today - timedelta(days=2)).isoformat(), "pending"),
    (405, 105, 3000, (today - timedelta(days=15)).isoformat(), "paid"),
    (406, 101, 4500, today.isoformat(), "pending")
])

cursor.executemany("""
    INSERT OR IGNORE INTO feedback
        (feedback_id, student_id, meal_id, rating, comments)
    VALUES (?, ?, ?, ?, ?)
""", [
    (501, 1, 201, 4, "Good breakfast"),
    (502, 2, 201, 3, "Average"),
    (503, 1, 202, 5, "Excellent lunch"),
    (504, 2, 206, 2, "Too spicy"),
    (505, 4, 205, 4, "Tasty"),
    (506, 5, 202, 2, "Needs improvement")
])

conn.commit()


# ==================================================
# 3. FIFTEEN BUSINESS QUERIES
# ==================================================

queries = [
    (
        "1. Display all students",
        """
        SELECT * FROM students
        ORDER BY student_id
        """,
        ()
    ),
    (
        "2. Display currently active subscriptions",
        """
        SELECT s.name, p.plan_name, sub.start_date, sub.end_date
        FROM subscriptions sub
        JOIN students s ON s.student_id = sub.student_id
        JOIN mess_plans p ON p.plan_id = sub.plan_id
        WHERE sub.status = 'active'
          AND sub.start_date <= date('now')
          AND sub.end_date >= date('now')
        ORDER BY s.name
        """,
        ()
    ),
    (
        "3. Students without an active subscription",
        """
        SELECT s.student_id, s.name
        FROM students s
        WHERE NOT EXISTS (
            SELECT 1
            FROM subscriptions sub
            WHERE sub.student_id = s.student_id
              AND sub.status = 'active'
              AND sub.start_date <= date('now')
              AND sub.end_date >= date('now')
        )
        ORDER BY s.student_id
        """,
        ()
    ),
    (
        "4. Number of subscriptions per plan",
        """
        SELECT p.plan_name, COUNT(sub.subscription_id) AS total
        FROM mess_plans p
        LEFT JOIN subscriptions sub ON sub.plan_id = p.plan_id
        GROUP BY p.plan_id, p.plan_name
        ORDER BY total DESC
        """,
        ()
    ),
    (
        "5. Total successful payment revenue",
        """
        SELECT COALESCE(SUM(amount), 0) AS total_revenue
        FROM payments
        WHERE status = 'paid'
        """,
        ()
    ),
    (
        "6. Monthly revenue report",
        """
        SELECT strftime('%Y-%m', payment_date) AS month,
               SUM(amount) AS revenue
        FROM payments
        WHERE status = 'paid'
        GROUP BY strftime('%Y-%m', payment_date)
        ORDER BY month
        """,
        ()
    ),
    (
        "7. Pending payments",
        """
        SELECT s.name, p.amount, p.payment_date, p.status
        FROM payments p
        JOIN subscriptions sub
            ON sub.subscription_id = p.subscription_id
        JOIN students s ON s.student_id = sub.student_id
        WHERE p.status = 'pending'
        ORDER BY p.payment_date
        """,
        ()
    ),
    (
        "8. Students who have paid more than Rs. 5000",
        """
        SELECT s.student_id, s.name, SUM(p.amount) AS total_paid
        FROM students s
        JOIN subscriptions sub ON sub.student_id = s.student_id
        JOIN payments p ON p.subscription_id = sub.subscription_id
        WHERE p.status = 'paid'
        GROUP BY s.student_id, s.name
        HAVING SUM(p.amount) > 5000
        ORDER BY total_paid DESC
        """,
        ()
    ),
    (
        "9. Attendance count for each meal",
        """
        SELECT m.meal_date, m.meal_type, m.menu,
               COUNT(a.attendance_id) AS attendance_count
        FROM meals m
        LEFT JOIN meal_attendance a
            ON a.meal_id = m.meal_id AND a.attended = 1
        GROUP BY m.meal_id, m.meal_date, m.meal_type, m.menu
        ORDER BY m.meal_date, m.meal_type
        """,
        ()
    ),
    (
        "10. Students with at least 3 attended meals",
        """
        SELECT s.name, COUNT(a.attendance_id) AS meals_attended
        FROM students s
        JOIN meal_attendance a ON a.student_id = s.student_id
        WHERE a.attended = 1
        GROUP BY s.student_id, s.name
        HAVING COUNT(a.attendance_id) >= 3
        ORDER BY meals_attended DESC
        """,
        ()
    ),
    (
        "11. Average rating for each meal type",
        """
        SELECT m.meal_type, ROUND(AVG(f.rating), 2) AS avg_rating
        FROM meals m
        JOIN feedback f ON f.meal_id = m.meal_id
        GROUP BY m.meal_type
        ORDER BY avg_rating DESC
        """,
        ()
    ),
    (
        "12. Meals with average rating below 3",
        """
        SELECT m.meal_date, m.meal_type, m.menu,
               ROUND(AVG(f.rating), 2) AS avg_rating
        FROM meals m
        JOIN feedback f ON f.meal_id = m.meal_id
        GROUP BY m.meal_id, m.meal_date, m.meal_type, m.menu
        HAVING AVG(f.rating) < 3
        ORDER BY avg_rating
        """,
        ()
    ),
    (
        "13. Students with no attendance in the last 7 days",
        """
        SELECT s.student_id, s.name
        FROM students s
        WHERE NOT EXISTS (
            SELECT 1
            FROM meal_attendance a
            JOIN meals m ON m.meal_id = a.meal_id
            WHERE a.student_id = s.student_id
              AND a.attended = 1
              AND m.meal_date >= date('now', '-6 days')
              AND m.meal_date <= date('now')
        )
        ORDER BY s.student_id
        """,
        ()
    ),
    (
        "14. Total successful revenue per mess plan",
        """
        SELECT p.plan_name,
               COALESCE(SUM(
                   CASE WHEN pay.status = 'paid'
                        THEN pay.amount ELSE 0 END
               ), 0) AS revenue
        FROM mess_plans p
        LEFT JOIN subscriptions sub ON sub.plan_id = p.plan_id
        LEFT JOIN payments pay
            ON pay.subscription_id = sub.subscription_id
        GROUP BY p.plan_id, p.plan_name
        ORDER BY revenue DESC
        """,
        ()
    ),
    (
        "15. Payment history for each student",
        """
        SELECT s.name, pay.amount, pay.payment_date, pay.status
        FROM students s
        JOIN subscriptions sub ON sub.student_id = s.student_id
        JOIN payments pay ON pay.subscription_id = sub.subscription_id
        ORDER BY s.name, pay.payment_date DESC
        """,
        ()
    )
]

for title, sql, params in queries:
    print(f"\n{title}")
    cursor.execute(sql, params)
    rows = cursor.fetchall()

    if rows:
        for row in rows:
            print(row)
    else:
        print("No records found.")


# ==================================================
# 4. OPTIMIZE AT LEAST THREE QUERIES
# ==================================================

# Index 1: Find subscriptions by student and status
cursor.execute("""
    CREATE INDEX IF NOT EXISTS idx_subscriptions_student_status
    ON subscriptions(student_id, status)
""")

# Index 2: Find payments by status and date
cursor.execute("""
    CREATE INDEX IF NOT EXISTS idx_payments_status_date
    ON payments(status, payment_date)
""")

# Index 3: Find attendance by student and meal
cursor.execute("""
    CREATE INDEX IF NOT EXISTS idx_attendance_student_meal
    ON meal_attendance(student_id, meal_id)
""")

conn.commit()

optimized_queries = [
    (
        "Optimization 1: Active subscriptions for a student",
        """
        SELECT *
        FROM subscriptions
        WHERE student_id = ? AND status = 'active'
        """,
        (1,)
    ),
    (
        "Optimization 2: Paid payments in date order",
        """
        SELECT payment_id, amount, payment_date
        FROM payments
        WHERE status = 'paid'
        ORDER BY payment_date
        """,
        ()
    ),
    (
        "Optimization 3: Attendance records for a student",
        """
        SELECT meal_id, attended
        FROM meal_attendance
        WHERE student_id = ?
        ORDER BY meal_id
        """,
        (1,)
    )
]

for title, sql, params in optimized_queries:
    print(f"\n{title}")
    print("Execution plan:")

    cursor.execute("EXPLAIN QUERY PLAN " + sql, params)
    for plan_row in cursor.fetchall():
        print(plan_row)

    cursor.execute(sql, params)
    print("Result:", cursor.fetchall())

conn.close()