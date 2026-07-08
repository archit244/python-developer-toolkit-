from storage import save_expenses,data
from utils import ask_for_input_number,ask_for_input_string,print_in_table_format
from datetime import date


def add_expense():
    name=ask_for_input_string("name")
    amount=ask_for_input_number("Enter Amount",0)
    category=ask_for_input_string("category")
    expense={
        "id":data["next_id"],
        "name": name,
        "amount": amount,
        "category": category,
        "date": str(date.today())
    }
    print("Expense added successfully")
    data["expenses"].append(expense)
    data["next_id"] += 1
    save_expenses()



def view_expenses():
    if(len(data["expenses"])==0):
        print("NO expenses")
    else:
        print_in_table_format(data["expenses"])

        
    

def search_expenses():
    query=ask_for_input_string("name")
    matched=[]
    for expense in data["expenses"]:
        if(expense["name"].lower().startswith(query.lower())):
            matched.append(expense)
    if(len(matched)==0):
        print("No matching expenses found.")
    else:
        print_in_table_format(matched)
    
def update_name(found_id):
    query=ask_for_input_string("name")
    data["expenses"][found_id]["name"]=query


def update_amount(found_id):
    query=ask_for_input_number("Enter Amount", 0)
    data["expenses"][found_id]["amount"]=query

def update_category(found_id):
    query=ask_for_input_string("category")
    data["expenses"][found_id]["category"]=query


def find_id(id):
    for i in range (len(data["expenses"])):
        if(data["expenses"][i]["id"]==id):
            return i
    return -1

def update_expense():
    UPDATE_ACTIONS={
    1: update_name,
    2: update_category,
    3: update_amount,
}
    query=ask_for_input_number("Enter ID",0)
    found_id=find_id(query)
    if(found_id==-1):
        print("Invalid ID")
        return
    print_in_table_format([data["expenses"][found_id]])
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
    print_in_table_format([data["expenses"][found_id]])
    data["expenses"].pop(found_id)
    print("Expense deleted successfully.")
    save_expenses()


def exit_program():
    print("goodbye")
    
