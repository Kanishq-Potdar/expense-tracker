from transactions import (
    add_transaction,
    view_transactions,
    search_transactions,
    filter_by_type,
    filter_by_date_range
)

from database import connect
import datetime

def main_menu():
    connect()  # Ensure DB exists

    while True:
        print("\n📋 Expense Tracker Menu")
        print("1. Add Transaction")
        print("2. View All Transactions")
        print("3. Search by Keyword")
        print("4. Filter by Type")
        print("5. Filter by Date Range")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == '1':
            handle_add_transaction()
        elif choice == '2':
            handle_view_transactions()
        elif choice == '3':
            handle_search_keyword()
        elif choice == '4':
            handle_filter_type()
        elif choice == '5':
            handle_filter_date_range()
        elif choice == '6':
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid choice.")


def handle_add_transaction():
    try:
        amount = float(input("Enter amount: "))
        type_ = input("Type (income/expense): ").strip().lower()
        if type_ not in ['income', 'expense']:
            print("❌ Type must be 'income' or 'expense'.")
            return

        category = input("Enter category (e.g., food, rent, etc.): ").strip()
        date_input = input("Enter date (YYYY-MM-DD) or press Enter for today: ").strip()

        if date_input == '':
            date = datetime.date.today().isoformat()
        else:
            try:
                date = datetime.datetime.strptime(date_input, '%Y-%m-%d').date().isoformat()
            except ValueError:
                print("❌ Invalid date format. Use YYYY-MM-DD.")
                return

        note = input("Enter note (optional): ")

        add_transaction(amount, type_, category, date, note)

    except ValueError:
        print("❌ Invalid input. Amount must be a number.")

def handle_view_transactions():
    transactions = view_transactions()
    if not transactions:
        print("📭 No transactions found.")
        return

    print("\n📄 All Transactions:")
    print("-" * 60)
    print(f"{'ID':<5} {'Amount':<10} {'Type':<8} {'Category':<12} {'Date':<12} {'Note'}")
    print("-" * 60)
    for txn in transactions:
        id_, amount, type_, category, date, note = txn
        print(f"{id_:<5} ₹{amount:<9.2f} {type_:<8} {category:<12} {date:<12} {note}")
    print("-" * 60)

def display_results(results):
    if not results:
        print("📭 No transactions found.")
        return

    print("\n📄 Matching Transactions:")
    print("-" * 60)
    print(f"{'ID':<5} {'Amount':<10} {'Type':<8} {'Category':<12} {'Date':<12} {'Note'}")
    print("-" * 60)
    for txn in results:
        id_, amount, type_, category, date, note = txn
        print(f"{id_:<5} ₹{amount:<9.2f} {type_:<8} {category:<12} {date:<12} {note}")
    print("-" * 60)

def handle_search_keyword():
    keyword = input("🔍 Enter keyword to search (note/category): ").strip()
    results = search_transactions(keyword)
    display_results(results)

def handle_filter_type():
    type_ = input("Filter type (income/expense): ").strip().lower()
    if type_ not in ['income', 'expense']:
        print("❌ Invalid type.")
        return
    results = filter_by_type(type_)
    display_results(results)

def handle_filter_date_range():
    start = input("Start date (YYYY-MM-DD): ").strip()
    end = input("End date (YYYY-MM-DD): ").strip()
    try:
        # Validate date format
        datetime.datetime.strptime(start, '%Y-%m-%d')
        datetime.datetime.strptime(end, '%Y-%m-%d')
        results = filter_by_date_range(start, end)
        display_results(results)
    except ValueError:
        print("❌ Invalid date format.")

if __name__ == '__main__':
    main_menu()
