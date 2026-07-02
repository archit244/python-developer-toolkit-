import os

def get_folder_path():
    while True:
        folder_path=input("Get Folder Path ").strip()
        if os.path.isdir(folder_path):
            return folder_path
        else:
            print("Invalid Folder Path, try again ")


def get_prefix():
    while True:
        prefix=input("Enter prefix Name ").strip()
        if len(prefix) >0 :
            return prefix
        else:
            print("Invalid prefix, try again ")

def validate_path(prefix,count,file,folder_path):
    ext=os.path.splitext(file)[1]
    while True:
        new_name=f"{prefix}_{count}{ext}"
        new_path=os.path.join(folder_path,new_name)
        if not os.path.exists(new_path):
            break
        count+=1
    return new_path,count


def rename_files(folder_path, prefix):
    files=os.listdir(folder_path)
    if not files:
        print("Folder is empty.")
        return
    count=1

    for file in files:
        file_path=os.path.join(folder_path,file)
        if not os.path.isfile(file_path):
            continue
        new_path,count=validate_path(prefix,count,file,folder_path)
 
        os.rename(file_path, new_path)
        print(f"Renamed {file} -> {os.path.basename(new_path)}")
        count+=1

    print(f"\nSuccessfully renamed all the files.")

def main():
    folder_path=get_folder_path()
    prefix=get_prefix()
    rename_files(folder_path,prefix)

main()