import json
import os.path
import time
from re import search


class Contact:
    def __init__(self):
        self.contacts = {}
        self.blocked = []
        self.load_contacts()

    def save_contacts(self):
        data = {"contacts":self.contacts, "blocked":self.blocked}
        with open("contacts.json", "w") as file:
            json.dump(data, file, indent=4)

    def load_contacts(self):
        if os.path.exists("contacts.json"):
            with open("contacts.json", "r") as file:
                data = json.load(file)
                self.contacts = data.get("contacts", {})
                self.blocked = data.get("blocked", [])

        else:
            self.contacts = {}
            self.blocked = []

    def add(self, name, number):
        self.contacts[name] = number
        self.save_contacts()

    def delete(self, name):
        if name in self.contacts:
            del self.contacts[name]
            self.save_contacts()
            print(f"{name} has been deleted.")
        else:
            print(f"{name} not found.")

    def block(self, name):
        if name in self.contacts:
            self.blocked.append(name)
            self.save_contacts()
            print(f"{name} has been blocked.")
        else:
            print(f"{name} not found.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts yet. Add contact.")
        else:
            for name, number in self.contacts.items():
                print(f"{name} : {number}")

    def search(self, query):
        found = False

        if query in self.contacts:
            print(f"Found: {query} : {self.contacts[query]}")
            found = True

        for name, number in self.contacts.items():
            if str(number) == query:
                print(f"Found: {name} : {number}")
                found = True

        if not found:
            print("There's no contact as such!")

def main():
    contact = Contact()
    while True:
        print("Welcome to your phonebook! \n 1.(V)iew contacts \n 2.(A)dd contact(s) \n 3.(D)elete Contact(s)"
                "\n OR 4.(B)lock contact(s) \n 5. Search for contacts \n 6.Quit")
        option = int(input('>'))
        if option == 1:
            contact.view_contacts()

        elif option == 2:
            print("Enter name of contact: ")
            NM = input('>')
            time.sleep(0.5)
            print(f"{NM}'s number: _ _ _ _ _ _ _ _ _ _ ")
            num = int(input('#>'))
            contact.add(NM,num)
            print("{NM} has been added.")
            contact.view_contacts()

        elif option == 3:
            print(f"Your contacts: \n {contact.view_contacts()}")
            time.sleep(0.5)
            print("Enter name of contact to be deleted")
            NM = input('>')
            print(f"Are you sure you want to delete {NM}? \n (Y)es or (N)o.")
            des = input('>').lower()
            if des == 'y':
                contact.delete(NM)
                time.sleep(1)
                print(f"{NM} has been deleted.")
            else:
                print("Deletion cancelled.")

        elif option == 4:
            print(f"Your contacts: \n {contact.view_contacts()}")
            time.sleep(0.5)
            print("Who are we blocking today?")
            NM = input('>')
            print(f"Block {NM}? \n (Y)es or (N)o.")
            des = input('>').lower()
            if des == 'y':
                contact.block(NM)
                time.sleep(1)
                print(f"{NM} has been deleted.")
            else:
                print("Deletion cancelled.")

        elif option == 5:
            print("Search by: \n 1. Name \n 2. Number")
            SC = input('>')
            if SC == '1':
                print("Enter name to be searched for: ")
                query = input('>').strip()
                contact.search(query)

            elif SC == '2':
                print("Enter name to be searched for: ")
                query = input('>').strip()
                contact.search(query)

            else:
                print("Invalid option, enter 1 or 2!")

        else:
            break
main()