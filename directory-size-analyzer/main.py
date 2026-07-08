import os

def get_folder_path():
    while True:
        folder_path=input("Enter folder path").strip()
        if os.path.isdir(folder_path):
            return folder_path
        print("Invalid path, try again")


def format_size(size):
    units=["B","KB","MB","GB","TB"]
    index=0
    while size>=1024 and index<len(units)-1:
        size/=1024
        index+=1
    return f"{size:.2f} {units[index]}"

def calculate_size(folder_path,indent):
    print(f'{"    " * (indent-1)}{os.path.basename(folder_path)}/')
    files = sorted(os.listdir(folder_path))
    total_size=0
    for file in files:
        if file.startswith("."):
            continue
        file_path=os.path.join(folder_path,file)
        if not os.path.isfile(file_path):
            total_size+= calculate_size(file_path,indent + 1)
            continue
        size=os.path.getsize(file_path)
        total_size+=size
        print(f'{"    " * indent}{file} ({format_size(size)})')
    print(f'{"    " * indent}Total: {format_size(total_size)}')
    print()
    return total_size



def main():
    folder_path=get_folder_path()
    size=calculate_size(folder_path,1)
main()