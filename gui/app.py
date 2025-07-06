import customtkinter as ctk
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from transactions import add_transaction, view_transactions
import datetime

ctk.set_appearance_mode("System")  # "Dark", "Light", or "System"
ctk.set_default_color_theme("blue")

class ExpenseTrackerApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Expense Tracker")
        self.geometry("700x500")

        # Top: Add Transaction
        self.add_frame = ctk.CTkFrame(self)
        self.add_frame.pack(pady=10, padx=10, fill="x")

        self.amount_entry = ctk.CTkEntry(self.add_frame, placeholder_text="Amount")
        self.amount_entry.grid(row=0, column=0, padx=5, pady=5)

        self.type_option = ctk.CTkOptionMenu(self.add_frame, values=["income", "expense"])
        self.type_option.set("expense")
        self.type_option.grid(row=0, column=1, padx=5, pady=5)

        self.category_entry = ctk.CTkEntry(self.add_frame, placeholder_text="Category")
        self.category_entry.grid(row=0, column=2, padx=5, pady=5)

        self.note_entry = ctk.CTkEntry(self.add_frame, placeholder_text="Note")
        self.note_entry.grid(row=0, column=3, padx=5, pady=5)

        self.add_button = ctk.CTkButton(self.add_frame, text="Add", command=self.handle_add)
        self.add_button.grid(row=0, column=4, padx=5, pady=5)

        self.message_label = ctk.CTkLabel(self, text="", text_color="green")
        self.message_label.pack()

        # Bottom: Transaction List
        self.listbox = ctk.CTkTextbox(self, height=350)
        self.listbox.pack(padx=10, pady=10, fill="both", expand=True)

        self.load_transactions()

    def handle_add(self):
        try:
            amount = float(self.amount_entry.get())
            type_ = self.type_option.get()
            category = self.category_entry.get()
            note = self.note_entry.get()
            date = datetime.date.today().isoformat()

            add_transaction(amount, type_, category, date, note)
            self.message_label.configure(text="Transaction added successfully!", text_color="green")
            self.clear_fields()
            self.load_transactions()
        except ValueError:
            self.message_label.configure(text="Invalid amount.", text_color="red")

    def clear_fields(self):
        self.amount_entry.delete(0, "end")
        self.category_entry.delete(0, "end")
        self.note_entry.delete(0, "end")

    def load_transactions(self):
        self.listbox.delete("0.0", "end")
        transactions = view_transactions()

        if not transactions:
            self.listbox.insert("end", "No transactions found.")
            return

        self.listbox.insert("end", f"{'ID':<4} {'Amount':<8} {'Type':<8} {'Category':<12} {'Date':<12} {'Note'}\n")
        self.listbox.insert("end", "-"*60 + "\n")

        for txn in transactions:
            id_, amount, type_, category, date, note = txn
            line = f"{id_:<4} ₹{amount:<8.2f} {type_:<8} {category:<12} {date:<12} {note}\n"
            self.listbox.insert("end", line)

# Run the GUI
if __name__ == "__main__":
    app = ExpenseTrackerApp()
    app.mainloop()
