import json

print("----Contact Book📝----")
print("1.View Contacts")
print("2.Add Contacts")
print("3.Delete all")
print("4.Delete a specific contact")
print("5.Edit a specific contact")

# ---------------- FUNCTIONS ----------------

def load_contacts():
    try:
        with open("contacts.json", "r") as f:
            return json.load(f)
    except:
        return {}   # return empty dictionary if file doesn't exist

def save_contacts(contacts):
    with open("contacts.json", "w") as f:
        json.dump(contacts, f, indent=4)
    print("Contacts saved!")

def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")
    
    contacts[name] = {"phone": phone, "email": email}
    save_contacts(contacts)

def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return
    
    print("\n--- All Contacts ---")
    for name, info in contacts.items():
        print(f"{name}: {info['phone']} | {info['email']}")

# ---------------- MAIN MENU ----------------

contacts = load_contacts()   # load BEFORE choice

def choice(status):
    match status:
        case 1:
            print("Viewing contacts...")
            view_contacts(contacts)

        case 2:
            print("Adding a contact...")
            add_contact(contacts)

        case 3:
            print("Deleting ALL contacts...")
            contacts.clear()
            save_contacts(contacts)

        case 4:
            print("Deleting a specific contact...")
            name = input("Enter name to delete: ")
            if name in contacts:
                del contacts[name]
                save_contacts(contacts)
                print("Contact deleted.")
            else:
                print("Contact not found!")

        case 5:
            print("Editing a contact...")
            name = input("Enter name to edit: ")
            if name in contacts:
                phone = input("New phone: ")
                email = input("New email: ")
                contacts[name] = {"phone": phone, "email": email}
                save_contacts(contacts)
                print("Contact updated.")
            else:
                print("Contact not found!")

        case _:
            print("Invalid choice!")

# RUN
user_choice = int(input("Enter your choice: "))
choice(user_choice)
