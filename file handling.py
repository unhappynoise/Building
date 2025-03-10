import os
def add_note():
    note = input("Write a note: ")
    title = input("Enter title of note: ") + ".txt"
    with open(title, "a") as file:
        file.write(note + "\n")

def view_note():
    files = os.listdir()
    txt_files = sorted([file for file in files if file.endswith(".txt")])

    if txt_files:
        print("\nAvailable notes:")
        for txt in txt_files:
            print(f"- {txt}")
    else:
        print("no notes found")

    title = input("Name of file to view: ") + ".txt"
    try:
        with open(title, "r") as file:
            details = file.read()
        if details.strip():
            print(details)
        else:
            print("File is empty")
    except FileNotFoundError:
        print(f"The file {title} does not exist")

def del_file():
    remove_file = input("Enter name of file to delete: ") + ".txt"
    if os.path.exists(remove_file):
        os.remove(remove_file)
        print(f"'{remove_file}' has been deleted")
    else:
        print(f"The file '{remove_file}' does not exist")

def rename():
    old_name = input("Enter name of file to rename: ") + ".txt"
    if os.path.exists(old_name):
        rename = input(f"Enter the new name for {old_name} file: ")+ ".txt"
        os.rename(old_name, rename)
        print(f"'{old_name}' has been renamed to '{rename}'")
    else:
        print(f"The file '{old_name}' doesn't exist")

def search_notes():
    search_term = input("Enter part of the file name to search for: ").lower()
    files = os.listdir()
    matches = [file for file in files if search_term in file.lower() and file.endswith(".txt")]

    if matches:
        print("\nMatching notes:")
        for match in matches:
            print(f"- {match}")
    else:
        print("No matching notes found")

def clear_note():
    title = input("Enter the name of the file to clear: ") + ".txt"
    if os.path.exists(title):
        with open(title, "w") as file:
            pass
        print(f"'{title}' has been cleared!")
    else:
        print(f"The file '{title}' does not exist")


def edit_note():
    title = input("Enter the name of the file to edit: ") + ".txt"

    if os.path.exists(title):
        choice = input("Do you want to append or overwrite the content (a/o)? ").strip().lower()

        if choice == "a":
            with open(title, "a") as file:
                new_content = input("Enter the content to add: ")
                file.write(new_content + "\n")
            print(f"New content has been added to '{title}'!")

        elif choice == "o":
            with open(title, "w") as file:
                new_content = input("Enter the new content: ")
                file.write(new_content + "\n")
            print(f"'{title}' has been updated!")

        else:
            print("Invalid choice! Please type 'a' to append or 'o' to overwrite.")

    else:
        print(f"The file '{title}' does not exist.")


while True:
    see = str(input("Add a new note, view existing note, rename a note, delete existing note, search for a note, edit or clear a note? (add/view/del/search/edit/clear) ")).strip().lower()
    if see == "add":
        add_note()
    elif see == "view":
        view_note()
    elif see == "rename":
        rename()
    elif see == "del":
        del_file()
    elif see == "search":
        search_notes()
    elif see == "clear":
        clear_note()
    elif see == "edit":
        edit_note()
    elif see == "exit":
        break
    else:
        print("Invalid choice! Please type 'add', 'view', 'rename', 'del', 'search', 'rename', 'edit' or 'exit' to quit.")