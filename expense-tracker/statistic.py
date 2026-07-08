from storage import data
from utils import print_key_value_table

def show_statistics():
    if len(data["expenses"]) == 0:
        print("No expenses")
        return
    statistics={}
    statistics["Total Expenses "]=len(data["expenses"])
    statistics["Total Amount   "]=sum(expense["amount"] for expense in data["expenses"])
    statistics["Highest Expense"]=max(expense["amount"] for expense in data["expenses"])
    statistics["Lowest Expense "]=min(expense["amount"] for expense in data["expenses"])
    statistics["Average Amount "]=round(statistics["Total Amount   "]/statistics["Total Expenses "],2)
    print_key_value_table("\n========== Statistics ==========",statistics)
    

def expenses_by_category():
    expenses_by_category={}
    for expense in data["expenses"]:
        if expense["category"] in expenses_by_category:
            expenses_by_category[expense["category"]]+=expense["amount"]
        else:
            expenses_by_category[expense["category"]]=expense["amount"]
    print_key_value_table("\n========== Expenses by category ==========",expenses_by_category)
