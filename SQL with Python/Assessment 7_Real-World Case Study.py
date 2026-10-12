
import sqlite3
from pathlib import Path

# Create a separate E-Commerce database
db_path = Path(__file__).parent / "ECommerce.db"

conn = sqlite3.connect(db_path)
conn.execute("PRAGMA foreign_keys = ON")
cursor = conn.cursor()

# 1. Create tables
cursor.execute("""
    CREATE TABLE IF NOT EXISTS customers (
        customer_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        city TEXT
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS orders (
        order_id INTEGER PRIMARY KEY,
        customer_id INTEGER,
        order_date TEXT NOT NULL,
        amount REAL NOT NULL,
        FOREIGN KEY (customer_id)
            REFERENCES customers(customer_id)
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        product_id INTEGER PRIMARY KEY,
        product_name TEXT NOT NULL,
        price REAL NOT NULL
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS order_items (
        order_id INTEGER,
        product_id INTEGER,
        quantity INTEGER NOT NULL CHECK (quantity > 0),
        PRIMARY KEY (order_id, product_id),
        FOREIGN KEY (order_id) REFERENCES orders(order_id),
        FOREIGN KEY (product_id) REFERENCES products(product_id)
    )
""")

# 2. Insert sample customers
cursor.executemany("""
    INSERT OR IGNORE INTO customers
        (customer_id, name, city)
    VALUES (?, ?, ?)
""", [
    (1, "Amit", "Ahmedabad"),
    (2, "Priya", "Mumbai"),
    (3, "Rahul", "Delhi"),
    (4, "Neha", "Ahmedabad"),
    (5, "Karan", "Pune")
])

# 3. Insert sample products
cursor.executemany("""
    INSERT OR IGNORE INTO products
        (product_id, product_name, price)
    VALUES (?, ?, ?)
""", [
    (1, "Laptop", 50000),
    (2, "Smartphone", 20000),
    (3, "Headphones", 5000),
    (4, "Keyboard", 2000)
])

# 4. Insert sample orders
cursor.executemany("""
    INSERT OR IGNORE INTO orders
        (order_id, customer_id, order_date, amount)
    VALUES (?, ?, ?, ?)
""", [
    (101, 1, "2026-01-15", 60000),
    (102, 2, "2026-01-20", 25000),
    (103, 1, "2026-02-10", 30000),
    (104, 3, "2026-02-18", 5000),
    (105, 4, "2026-03-05", 55000),
    (106, 2, "2026-03-12", 30000)
])

# 5. Insert sample order items
cursor.executemany("""
    INSERT OR IGNORE INTO order_items
        (order_id, product_id, quantity)
    VALUES (?, ?, ?)
""", [
    (101, 1, 1),
    (101, 3, 2),
    (102, 2, 1),
    (102, 3, 1),
    (103, 2, 1),
    (103, 3, 2),
    (104, 4, 1),
    (105, 1, 1),
    (105, 3, 1),
    (106, 2, 1),
    (106, 3, 2)
])

conn.commit()

# Task 1: Total orders per customer
print("\n1. Total Orders Per Customer")

cursor.execute("""
    SELECT c.customer_id, c.name,
           COUNT(o.order_id) AS total_orders
    FROM customers c
    LEFT JOIN orders o
        ON c.customer_id = o.customer_id
    GROUP BY c.customer_id, c.name
    ORDER BY c.customer_id
""")

for row in cursor.fetchall():
    print(row)


# Task 2: Customers who never placed an order
print("\n2. Customers Who Never Placed an Order")

cursor.execute("""
    SELECT c.customer_id, c.name, c.city
    FROM customers c
    LEFT JOIN orders o
        ON c.customer_id = o.customer_id
    WHERE o.order_id IS NULL
""")

for row in cursor.fetchall():
    print(row)


# Task 3: Highest-selling product by quantity
print("\n3. Highest-Selling Product")

cursor.execute("""
    SELECT p.product_id, p.product_name,
           SUM(oi.quantity) AS total_sold
    FROM products p
    JOIN order_items oi
        ON p.product_id = oi.product_id
    GROUP BY p.product_id, p.product_name
    ORDER BY total_sold DESC
    LIMIT 1
""")

print(cursor.fetchone())


# Task 4: Monthly sales report
print("\n4. Monthly Sales Report")

cursor.execute("""
    SELECT strftime('%Y-%m', order_date) AS month,
           ROUND(SUM(amount), 2) AS monthly_sales
    FROM orders
    GROUP BY strftime('%Y-%m', order_date)
    ORDER BY month
""")

for row in cursor.fetchall():
    print(row)


# Task 5: Customers with total purchases above Rs. 50,000
print("\n5. Customers With Purchases Above Rs. 50,000")

cursor.execute("""
    SELECT c.customer_id, c.name,
           SUM(o.amount) AS total_purchase
    FROM customers c
    JOIN orders o
        ON c.customer_id = o.customer_id
    GROUP BY c.customer_id, c.name
    HAVING SUM(o.amount) > 50000
    ORDER BY total_purchase DESC
""")

for row in cursor.fetchall():
    print(row)


# Task 6: Top 3 cities by revenue
print("\n6. Top 3 Cities By Revenue")

cursor.execute("""
    SELECT c.city, SUM(o.amount) AS revenue
    FROM customers c
    JOIN orders o
        ON c.customer_id = o.customer_id
    GROUP BY c.city
    ORDER BY revenue DESC
    LIMIT 3
""")

for row in cursor.fetchall():
    print(row)


conn.close()