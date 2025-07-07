import sqlite3
from database import get_db_connection

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

# Search transactions by keyword (note or category)
def search_transactions(keyword):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute('''
        SELECT * FROM transactions
        WHERE note LIKE ? OR category LIKE ?
        ORDER BY date DESC
    ''', (f'%{keyword}%', f'%{keyword}%'))

    results = cursor.fetchall()
    conn.close()
    return results


# Filter transactions by type (income or expense)
def filter_by_type(type_):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute('''
        SELECT * FROM transactions
        WHERE type = ?
        ORDER BY date DESC
    ''', (type_,))

    results = cursor.fetchall()
    conn.close()
    return results


# Filter transactions by date range
def filter_by_date_range(start_date, end_date):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute('''
        SELECT * FROM transactions
        WHERE date BETWEEN ? AND ?
        ORDER BY date DESC
    ''', (start_date, end_date))

    results = cursor.fetchall()
    conn.close()
    return results
def get_monthly_summary():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('''
        SELECT 
            strftime('%Y-%m', date) AS month,
            SUM(CASE WHEN type = 'income' THEN amount ELSE 0 END) AS total_income,
            SUM(CASE WHEN type = 'expense' THEN amount ELSE 0 END) AS total_expense
        FROM transactions
        GROUP BY month
        ORDER BY month DESC
    ''')

    summary = cursor.fetchall()
    conn.close()
    return summary

import csv

def export_to_csv(transactions, filename="transactions_export.csv"):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Amount", "Type", "Category", "Date", "Note"])  # header
        for txn in transactions:
            writer.writerow(txn)

