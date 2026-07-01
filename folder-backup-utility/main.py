import os
import shutil

def get_folder_path():
    while True: 
        folder_path=input("Enter folder path ").strip()
        if(os.path.isdir(folder_path)):
            return folder_path
        else :
            print("Invalid folder path. Please try again.")

def backup_folder(folder_path,backup_path):
    files=os.listdir(folder_path)
    for file in files:
        file_path=os.path.join(folder_path,file)
        if not os.path.isfile(file_path):
            next_path=os.path.join(backup_path,file)
            os.makedirs(next_path,exist_ok=True)
            backup_folder(file_path,next_path)
            continue
        if file.startswith("."):
            continue
        shutil.copy2(file_path,backup_path)
        print(f"copied {file_path} to {backup_path}")

def get_unique_path(path):
    if os.path.isdir(path):
        a=1
        while(os.path.isdir(path)):
            base_name=os.path.basename(path)
            parent=os.path.dirname(path)
            path=os.path.join(parent,f"{base_name}({a})")
            a+=1
    return path   


def main():
    folder_path=get_folder_path()

    parent = os.path.dirname(folder_path)
    base_name=os.path.basename(folder_path)

    backup_path=os.path.join(parent,f"{base_name}_backup")
    checked_backup_path=get_unique_path(backup_path)

    os.makedirs(checked_backup_path)
    backup_folder(folder_path,checked_backup_path)

main()