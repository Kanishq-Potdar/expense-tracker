from transactions import add_transaction, view_transactions
from database import connect
import datetime

def main_menu():
    connect()  # Ensure DB is created before anything

    while True:
        print("\n📋 Expense Tracker Menu")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Exit")

        choice = input("Choose an option (1-3): ")

        if choice == '1':
            handle_add_transaction()
        elif choice == '2':
            handle_view_transactions()
        elif choice == '3':
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please enter 1, 2, or 3.")

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


if __name__ == '__main__':
    main_menu()
