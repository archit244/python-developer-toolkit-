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

def ask_for_input_string(field):
    name=""
    while True:
        name=input(f"Enter expense {field}. ").strip()
        if(name!=""):
            break
        else:
            print("Invalid")
    return name

def print_key_value_table(title,subjects):
    print(title)
    for subject in subjects:
        print(f"{subject} : {subjects[subject]}")   

        
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
