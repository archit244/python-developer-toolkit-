# 💰 Expense Tracker

A command-line Expense Tracker built in Python that allows users to manage their daily expenses with persistent JSON storage.

This project is part of the **Python Developer Toolkit**, a collection of small command-line utilities built to strengthen Python fundamentals through hands-on practice.

---

## ✨ Features

- ➕ Add new expenses
- 📋 View all expenses in a formatted table
- 🔍 Search expenses by name
- ✏️ Update existing expenses
- 🗑️ Delete expenses
- 📊 View overall expense statistics
- 📂 View category-wise expense totals
- 💾 Automatic JSON data persistence
- 🆔 Auto-generated unique expense IDs
- 📅 Automatic date generation
- ✅ Input validation

---

## 🛠️ Tech Stack

- Python 3
- Standard Library
  - `json`
  - `datetime`

---

## 📁 Project Structure

```text
expense-tracker/
│── main.py
│── menu.py
│── operations.py
│── statistics.py
│── storage.py
│── utils.py
│── expenses.json
│── README.md
│── requirements.md
│── design.md
└── userflow.md
```

---

## 🚀 Getting Started

Clone the repository:

```bash
git clone <repository-url>
cd expense-tracker
```

Run the application:

```bash
python3 main.py
```

---

## 📸 Sample Menu

```text
========================================
        EXPENSE TRACKER
========================================

1. Add Expense
2. View Expenses
3. Search Expenses
4. Update Expense
5. Delete Expense
6. View Statistics
7. View Category Summary
8. Exit

========================================
Choose an option:
```

---

## 📚 Concepts Practiced

This project was built as part of a hands-on Python fundamentals series, focusing on solving practical problems while learning core programming concepts.

- Functions
- Lists & Dictionaries
- CRUD Operations
- JSON File Handling
- Exception Handling
- Input Validation
- Dictionary Dispatch
- Helper Functions
- String Formatting
- Data Persistence
- Aggregations (`sum`, `max`, `min`)
- Python Modules & Imports
- Project Organization
- Basic Software Design

---

## 🎯 Future Improvements

- Export expenses to CSV
- Filter expenses by date
- Sort expenses by amount or date
- Monthly and yearly expense reports
- Budget tracking
- Charts and visualizations
- SQLite database support

---

## 📜 License

This project is intended for learning and educational purposes.