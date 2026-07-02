import os
import json

def get_file_path():
    while True:
        file_path=input("enter file path")
        if file_path.endswith(".json") and os.path.isfile(file_path):
            return file_path
        print("Invalid path, try again")

def validate_json(file_path):
    try:
        with open(file_path,"r") as file:
            data=json.load(file)
            return data
    except json.JSONDecodeError:
        print("invalid json")
        return None
        
def format_json(file_path,data):
    parent=os.path.dirname(file_path)
    base_name=os.path.splitext(os.path.basename(file_path))[0]
    formatted_path=os.path.join(parent,f"{base_name}_formatted.json")
    with open(formatted_path,"w") as file:
        json.dump(data,file,indent=4)
    print(f"Formatted JSON saved to: {formatted_path}")
    
def main():
    file_path=get_file_path()
    data=validate_json(file_path)
    if data is None:
        return
    format_json(file_path, data)

    