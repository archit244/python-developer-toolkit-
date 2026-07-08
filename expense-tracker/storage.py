import json

data = {
    "expenses": [],
    "next_id": 1
}

def save_expenses():
    with open("expenses.json", "w") as file:
        json.dump(data, file,indent=4)

def load_expenses():
    try:
        with open("expenses.json", "r") as file:
            loaded_data=json.load(file)
            data["expenses"]=loaded_data["expenses"]
            data["next_id"]=loaded_data["next_id"]
    except FileNotFoundError:
        data["expenses"]=[]
        data["next_id"]=1 

        