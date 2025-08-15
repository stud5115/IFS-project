import sqlite3

def init_db():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            leave_balance INTEGER NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def add_employee(name, leave_balance):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO employees (name, leave_balance) VALUES (?, ?)", (name, leave_balance))
    conn.commit()
    conn.close()

def get_leave_balance(name):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT leave_balance FROM employees WHERE name = ?", (name,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None

def apply_leave(name, days):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT leave_balance FROM employees WHERE name = ?", (name,))
    result = cursor.fetchone()
    if result and result[0] >= days:
        new_balance = result[0] - days
        cursor.execute("UPDATE employees SET leave_balance = ? WHERE name = ?", (new_balance, name))
        conn.commit()
        conn.close()
        return True
    conn.close()
    return False

# Run this once to create the database and add sample data
if __name__ == "__main__":
    init_db()
    add_employee("Alice", 15)
    add_employee("Bob", 10)
