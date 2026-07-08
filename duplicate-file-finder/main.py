import os
import hashlib

def get_folder_path():
    while True:
        folder_path=input("Enter folder path: ").strip()
        if os.path.isdir(folder_path):
            return folder_path
        print("Invalid path")

def generate_hash(file_path):
     with open(file_path, "rb") as item:
        fingerprint = hashlib.sha256(item.read()).hexdigest()
        return fingerprint
        
def find_duplicates(folder_path):
    print("Scanning files...")
    duplicates = {}
    files=os.listdir(folder_path)
    for file in files:
        file_path=os.path.join(folder_path,file)
        if not os.path.isfile(file_path):
            continue
        fingerprint=generate_hash(file_path)
        if fingerprint in duplicates:
            duplicates[fingerprint].append(file_path)
        else:
            duplicates[fingerprint]=[file_path]
    return duplicates

def display_duplicates(duplicates):
    duplicate_found = False
    group = 1
    print("\n===== Duplicate Files =====\n")
    for files in duplicates.values():
        if len(files) > 1:
            duplicate_found = True
            print(f"Group {group}:")
            for file in files:
                print(f"  - {os.path.basename(file)}")
            print()
            group += 1
    print(f"\nDuplicate groups found: {group - 1}")
    if not duplicate_found:
        print("No duplicate files found.")

def ask_for_permission():
    while True:
        choice=input("Do you want to delete duplicates?(y/n)")
        if choice.lower() in ("y","n"):
            return choice.lower()
        print("Invalid input, try again")

def delete_duplicates(duplicates):
    for files in duplicates.values():
        if len(files)==1:
            continue
        oldest=min(files,key=os.path.getmtime)
        print(f"\nKept: {os.path.basename(oldest)}")
        for file in files:
            if file!=oldest:
                os.remove(file)
                print(f"Deleted: {os.path.basename(file)}")
    print("\nDuplicate cleanup completed.")
    
def main():
    folder_path=get_folder_path()
    duplicates=find_duplicates(folder_path)
    display_duplicates(duplicates)
    choice=ask_for_permission()
    if choice=="y":
        delete_duplicates(duplicates)
    
   
main()

