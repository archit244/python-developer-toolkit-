from operations import add_expense,view_expenses,search_expenses,update_expense,delete_expense,exit_program
from statistic import show_statistics,expenses_by_category
from utils import ask_for_input_number

def main_menu():
    while True:
        option = ask_for_input_number(
    """
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
Choose an option: """,
    1,
    8
)
        ACTIONS[option]()
        if(option==8):
            break


ACTIONS = {
    1: add_expense,
    2: view_expenses,
    3: search_expenses,
    4: update_expense,
    5: delete_expense,
    6: show_statistics,
    7: expenses_by_category,
    8: exit_program,
}


