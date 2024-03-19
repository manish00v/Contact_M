#Contact Management System

import csv
import re

#validate email

def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

#validate phone number with country code

def is_valid_phone(phone):
    pattern = r'^(?:(?:\+|0{0,2})91(\s*[\-]\s*)?|[0]?)?[789]\d{9}$'
    return re.match(pattern, phone) is not None

def add_contact(contacts):
    name = input("Please enter contact name: ")
    phone = input("Please enter contact phone number: ")
    email = input("Please enter contact email: ")
    
    if name.strip() == "":
        print("Invalid name. Contact not added.")
        return
    
    if not is_valid_email(email):
        print("Invalid email. Contact not added.")
        return
    
    if not is_valid_phone(phone):
        print("Invalid phone number. Contact not added.")
        return
    
    contacts[name] = {"Phone": phone, "Email": email}
    print("Contact added successfully.")

#search contact by name

def search_contact(contacts):
    name = input("Please enter contact name to search: ")
    contact = contacts.get(name)
    
    if contact:
        print("Name:", name)
        print("Phone:", contact["Phone"])
        print("Email:", contact["Email"])
    else:
        print("Contact not found.")

#update contact information

def update_contact(contacts):
    name = input("Please enter contact name to update: ")
    contact = contacts.get(name)
    
    if contact:
        print("Current contact information:")
        print("Name:", name)
        print("Phone:", contact["Phone"])
        print("Email:", contact["Email"])
        
        new_phone = input("Please enter new phone number: ")
        new_email = input("Please enter new email address: ")
        
        contact["Phone"] = new_phone if new_phone else contact["Phone"]
        contact["Email"] = new_email if new_email else contact["Email"]
        
        print("Contact information updated.")
    else:
        print("Contact not found.")

#load contacts from CSV file

def load_contacts_from_file(filename):
    contacts = {}
    try:
        with open(filename, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) == 3:
                    name, phone, email = row
                    contacts[name] = {"Phone": phone, "Email": email}
        print("Contacts loaded successfully.")
    except IOError:
        print("Error occurred while loading contacts from file.")
    
    return contacts
def main():
    contacts = {}
    filename = "contacts.csv"  
    contacts = load_contacts_from_file(filename)
    
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. Exit")
        
        choice = input("Please enter your choice (1-4): ")
        
        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            search_contact(contacts)
        elif choice == "3":
            update_contact(contacts)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")
    print("Thank You!")
    
if __name__ == "__main__":
    main()