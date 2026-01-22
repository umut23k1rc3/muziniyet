import sqlite3

def init_db():
    conn = sqlite3.connect("career.db")
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        interest TEXT
    )
    """)

    conn.commit()
    conn.close()

def save_interest(user_id, interest):
    conn = sqlite3.connect("career.db")
    cur = conn.cursor()
    cur.execute(
        "INSERT OR REPLACE INTO users (user_id, interest) VALUES (?, ?)",
        (user_id, interest)
    )
    conn.commit()
    conn.close()

def get_interest(user_id):
    conn = sqlite3.connect("career.db")
    cur = conn.cursor()
    cur.execute("SELECT interest FROM users WHERE user_id=?", (user_id,))
    row = cur.fetchone()
    conn.close()
    return row[0] if row else None
