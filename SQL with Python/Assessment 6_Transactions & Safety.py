import sqlite3
from pathlib import Path

db_path = Path(__file__).parent / "College.db"

conn = sqlite3.connect(db_path)
cursor = conn.cursor()


# Create accounts table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS accounts (
        account_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        balance REAL NOT NULL
    )
""")

# Add sample accounts only if they don't exist
cursor.execute("""
    INSERT OR IGNORE INTO accounts (account_id, name, balance)
    VALUES (1, 'Rahul', 5000)
""")

cursor.execute("""
    INSERT OR IGNORE INTO accounts (account_id, name, balance)
    VALUES (2, 'Amit', 3000)
""")

conn.commit()


# 1. Start a transaction
try:
    conn.execute("BEGIN")

    # 2. Insert record into accounts
    cursor.execute("""
        INSERT INTO accounts (account_id, name, balance)
        VALUES (?, ?, ?)
    """, (3, "Priya", 4000))

    print("Record inserted inside transaction.")


    # 3. Rollback changes
    conn.rollback()

    print("Transaction rolled back.")


except sqlite3.Error as e:
    conn.rollback()
    print("Transaction failed:", e)


# 4. Commit a valid transaction
try:
    conn.execute("BEGIN")

    cursor.execute("""
        INSERT INTO accounts (account_id, name, balance)
        VALUES (?, ?, ?)
    """, (3, "Priya", 4000))

    conn.commit()

    print("Valid transaction committed successfully.")

except sqlite3.Error as e:
    conn.rollback()
    print("Transaction failed:", e)


# 5. Demonstrate money transfer
try:
    conn.execute("BEGIN")

    sender = 1
    receiver = 2
    amount = 1000

    # Check sender balance
    cursor.execute(
        "SELECT balance FROM accounts WHERE account_id = ?",
        (sender,)
    )

    balance = cursor.fetchone()[0]

    if balance < amount:
        raise Exception("Insufficient balance")

    # Deduct money from sender
    cursor.execute("""
        UPDATE accounts
        SET balance = balance - ?
        WHERE account_id = ?
    """, (amount, sender))

    # Add money to receiver
    cursor.execute("""
        UPDATE accounts
        SET balance = balance + ?
        WHERE account_id = ?
    """, (amount, receiver))

    # Everything successful
    conn.commit()

    print("Money transferred successfully.")

except Exception as e:
    conn.rollback()
    print("Transfer failed:", e)


# Display final accounts
print("\nAccount Details:")

cursor.execute("SELECT * FROM accounts")

for account in cursor.fetchall():
    print(account)
