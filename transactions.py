import sqlite3

DB_PATH = 'data/tracker.db'

# Function to add a new transaction
def add_transaction(amount, type_, category, date, note):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO transactions (amount, type, category, date, note)
        VALUES (?, ?, ?, ?, ?)
    ''', (amount, type_, category, date, note))

    conn.commit()
    conn.close()
    print("✅ Transaction added successfully!")


# Function to view all transactions
def view_transactions():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM transactions ORDER BY date DESC')
    rows = cursor.fetchall()

    conn.close()
    return rows
