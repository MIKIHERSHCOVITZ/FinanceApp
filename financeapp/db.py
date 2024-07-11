import sqlite3

def init_db():
    with sqlite3.connect('financial_data.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT,
                password TEXT
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS financial_data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                insurance TEXT,
                pension REAL,
                bank_balance REAL,
                loan REAL,
                credit_card TEXT,
                salary REAL,
                savings REAL,
                investments REAL,
                FOREIGN KEY (user_id) REFERENCES users(id)
            )
        ''')
    conn.close()
