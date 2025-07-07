# Expense Tracker

A lightweight, modular desktop application to track income and expenses with a clean, modern GUI built using Python and `customtkinter`. Designed to help users record, filter, summarize, and export their financial activity easily.

## Features

- Add income and expense transactions with categories and notes
- View all transactions in a scrollable, formatted list
- Filter/search by keyword, type, and date range
- View monthly summary with income, expenses, and net savings
- Export filtered transactions to CSV
- Persistent data storage using SQLite

## Tech Stack

- Language: Python 3
- GUI: customtkinter
- Database: SQLite
- Others: CSV for export functionality

## Upcoming Features

- Visualizations of expense/income distribution (pie and bar charts)
- Calendar-based transaction view
- Budget limit alerts

## How to Run

1. Clone the repo:
   git clone https://github.com/Kanishq-Potdar/expense-tracker.git
   cd expense-tracker

2. Install required packages:
   pip install customtkinter

3. Run the app:
   python gui/app.py

(Make sure you're using Python 3.8 or later)

## Project Structure

expense-tracker/
├── gui/
│ └── app.py # Main GUI application  
├── transactions.py # Logic for add/view/export/filter  
├── database.py # SQLite DB setup and connection  
├── data/
│ └── tracker.db # Local database (auto-generated)  
├── README.md

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss the idea.
