import sqlite3
import os

# This function connects to the database (creates if it doesn't exist)
def connect():
    if not os.path.exists('data'):
        os.makedirs('data')

    conn = sqlite3.connect('data/tracker.db')
    cursor = conn.cursor()

    # Create the transactions table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount REAL NOT NULL,
            type TEXT CHECK(type IN ('income', 'expense')) NOT NULL,
            category TEXT,
            date TEXT NOT NULL,
            note TEXT
        )
    ''')

    conn.commit()
    conn.close()

def get_db_connection():
    return sqlite3.connect('data/tracker.db')


# Call connect only if this file is run directly
if __name__ == '__main__':
    connect()
