import sqlite3
from pathlib import Path

db_path = Path(__file__).parent / "College.db"

conn = sqlite3.connect(db_path)

# Enable foreign key support in SQLite
conn.execute("PRAGMA foreign_keys = ON")

cursor = conn.cursor()


# 1. Create users table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        name TEXT,
        email TEXT UNIQUE,
        password TEXT NOT NULL
    )
""")

print("1. Users table created successfully.")


# 2. Create orders table with foreign key
cursor.execute("""
    CREATE TABLE IF NOT EXISTS orders (
        order_id INTEGER PRIMARY KEY,
        user_id INTEGER,
        amount REAL,
        FOREIGN KEY (user_id) REFERENCES users(user_id)
    )
""")

print("2. Orders table with foreign key created successfully.")


# 3. Create index on email
cursor.execute("""
    CREATE INDEX IF NOT EXISTS idx_users_email
    ON users(email)
""")

print("3. Index on email created successfully.")


# 4. Create view for user order summary
cursor.execute("""
    CREATE VIEW IF NOT EXISTS user_order_summary AS
    SELECT
        users.user_id,
        users.name,
        users.email,
        COUNT(orders.order_id) AS total_orders,
        COALESCE(SUM(orders.amount), 0) AS total_amount
    FROM users
    LEFT JOIN orders
        ON users.user_id = orders.user_id
    GROUP BY users.user_id
""")

print("4. User order summary view created successfully.")


conn.commit()