import json
from datetime import date

expenses=[] 
next_id=1


def ask_for_input_number(field,start,end=None):
    number=""
    while True:
        number=input(f"{field}")
        try:
            number=int(number)
        except ValueError:
            print("Invalid")
            continue
        if number >= start and (end is None or number <= end):
            break
        else:
             print("Invalid")
    return number

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


def ask_for_input_string(field):
    name=""
    while True:
        name=input(f"Enter expense {field}. ").strip()
        if(name!=""):
            break
        else:
            print("Invalid")
    return name


def add_expense():
    global next_id
    name=ask_for_input_string("name")
    amount=ask_for_input_number("Enter Amount",0)
    category=ask_for_input_string("category")
    expense={
        "id":next_id,
        "name": name,
        "amount": amount,
        "category": category,
        "date": str(date.today())
    }
    print("Expense added successfully")
    expenses.append(expense)
    next_id += 1
    save_expenses()

def print_in_table_format(expenses):
    print(f"{'ID':<4}{'Name':<20}{'Amount':<10}{'Category':<15}{'Date':<12}")
    print("-" * 61)
    for expense in expenses:
        print(
        f"{expense['id']:<4} "
        f"{expense['name']:<20} "
        f"{expense['amount']:<10} "
        f"{expense['category']:<15} "
        f"{expense['date']:<12}"
          )


def view_expenses():
    if(len(expenses)==0):
        print("NO expenses")
    else:
        print_in_table_format(expenses)

        
    

def search_expenses():
    query=ask_for_input_string("name")
    matched=[]
    for expense in expenses:
        if(expense["name"].lower().startswith(query.lower())):
            matched.append(expense)
    if(len(matched)==0):
        print("No matching expenses found.")
    else:
        print_in_table_format(matched)
    
def update_name(found_id):
    query=ask_for_input_string("name")
    expenses[found_id]["name"]=query


def update_amount(found_id):
    query=ask_for_input_number("Enter Amount", 0)
    expenses[found_id]["amount"]=query

def update_category(found_id):
    query=ask_for_input_string("category")
    expenses[found_id]["category"]=query


def find_id(id):
    for i in range (len(expenses)):
        if(expenses[i]["id"]==id):
            return i
    return -1

def update_expense():
    query=ask_for_input_number("Enter ID",0)
    found_id=find_id(query)
    if(found_id==-1):
        print("Invalid ID")
        return
    print_in_table_format([expenses[found_id]])
    option = ask_for_input_number(
    """
========================================
         UPDATE EXPENSE
========================================

1. Update Name
2. Update Category
3. Update Amount

========================================
Choose an option: """,
    1,
    3
)
    UPDATE_ACTIONS[option](found_id)
    save_expenses()
        


def delete_expense():
    query=ask_for_input_number("Enter ID",0)
    found_id=find_id(query)
    if(found_id==-1):
        print("Invalid ID")
        return
    print_in_table_format([expenses[found_id]])
    expenses.pop(found_id)
    print("Expense deleted successfully.")
    save_expenses()

def print_key_value_table(title,subjects):
    print(title)
    for subject in subjects:
        print(f"{subject} : {subjects[subject]}")   
    
    

def show_statistics():
    if len(expenses) == 0:
        print("No expenses")
        return
    statistics={}
    statistics["Total Expenses "]=len(expenses)
    statistics["Total Amount   "] = sum(expense["amount"] for expense in expenses)
    statistics["Highest Expense"] = max(expense["amount"] for expense in expenses)
    statistics["Lowest Expense "] = min(expense["amount"] for expense in expenses)
    statistics["Average Amount "]=round(statistics["Total Amount   "]/statistics["Total Expenses "],2)
    print_key_value_table("\n========== Statistics ==========",statistics)
    

def expenses_by_category():
    expenses_by_category={}
    for expense in expenses:
        if expense["category"] in expenses_by_category:
            expenses_by_category[expense["category"]]+=expense["amount"]
        else:
            expenses_by_category[expense["category"]]=expense["amount"]
    print_key_value_table("\n========== Expenses by category ==========",expenses_by_category)


def exit_program():
    print("goodbye")
    

def save_expenses():
    with open("expenses.json", "w") as file:
        data = {
            "next_id": next_id,
            "expenses": expenses
        }
        json.dump(data, file,indent=4)
def load_expenses():
    global expenses
    global next_id
    try:
        with open("expenses.json", "r") as file:
            data=json.load(file)
            expenses=data["expenses"]
            next_id=data["next_id"]
    except FileNotFoundError:
        expenses=[]
        next_id=1

        

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
UPDATE_ACTIONS={
    1: update_name,
    2: update_category,
    3: update_amount,
}
load_expenses()
main_menu()