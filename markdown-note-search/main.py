import os

def get_folder_path():
    while True:
        folder_path=input("Enter Folder Name").strip()
        if(os.path.isdir(folder_path)):
            return folder_path
        print("Invalid Path Try again")

def get_keyword():
    while True:
        keyword=input("enter keyword name").strip()
        if keyword:
            return keyword
        print("Invalid keyword Try again")

def search_note(keyword,file_path):
    found=[]
    with open(file_path, "r") as file:
        for line_number,line in enumerate(file,start=1):
            if keyword.lower() in line.lower():
                found.append((line_number,line.strip()))
    return found
    

def check_md(folder_path,keyword):
    files=os.listdir(folder_path)
    lines_found={}
    for file in files:
        if file.endswith(".md"):
            file_path=os.path.join(folder_path,file)
            found=search_note(keyword,file_path)
            if found:
                lines_found[file]=found
    return lines_found

def output(lines_found):
    if not lines_found:
        print("No matches found.")
        return
    total_matches=0
    for filename, matches in lines_found.items():
        print(filename)
        for line_number, text in matches:
            print(f"  Line {line_number}: {text}")
            total_matches+=1
        print()
    print("----------------------------------")
    print()
    print(f"Files matched: {len(lines_found)}")
    print(f"Total matches: {total_matches}")



def main():
    folder_path=get_folder_path()
    keyword=get_keyword()
    lines_found=check_md(folder_path,keyword)
    output(lines_found)

main()