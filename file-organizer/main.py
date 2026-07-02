import os
import shutil
from file_types import FILE_TYPES

def get_folder_path():
    while True: 
        folder_path=input("Enter folder path ").strip()
        if(os.path.isdir(folder_path)):
            return folder_path
        else :
            print("Invalid folder path. Please try again.")

def organize_files(folder_path):
        files = os.listdir(folder_path)
        for file in files:
            item_path = os.path.join(folder_path, file)

            if not os.path.isfile(item_path):
                continue

            extension=os.path.splitext(file)[1]
            category=FILE_TYPES.get(extension,"Others")
            destination_folder=os.path.join(folder_path,category)

            os.makedirs(destination_folder,exist_ok=True)
            shutil.move(item_path, destination_folder)

            print(f"moving {file} to {category}")


def main():
    folder_path=get_folder_path()
    organize_files(folder_path)

main()