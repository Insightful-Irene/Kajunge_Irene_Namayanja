contacts = [
    {"id": 1, "name": "Joy",        "phone": "0700000001", "email": "joy@gmail.com"},
    {"id": 2, "name": "Insightful", "phone": "0700000002", "email": "insightful@gmail.com"},
    {"id": 3, "name": "Zoe",        "phone": "0700000003", "email": "zoe@yahoo.com"},
    {"id": 4, "name": "Elijah",     "phone": "0700000004", "email": "elijah@outlook.com"},
    {"id": 5, "name": "Grace",      "phone": "0700000005", "email": "grace@gmail.com"},
    {"id": 6, "name": "David",      "phone": "0700000006", "email": "david@yahoo.com"}
]

next_id = 7


# Task 1: Validation

validate_phone = lambda phone: (
    phone.startswith("07") and
    len(phone) == 10 and
    all(char.isdigit() for char in phone)
)

validate_email = lambda email: (
    email == "" or
    ("@" in email and "." in email)
)


# Helper: Print One Contact

def print_contact(contact):
    print("ID    : " + str(contact["id"]))
    print("Name  : " + contact["name"])
    print("Phone : " + contact["phone"])

    if contact["email"] == "":
        print("Email : N/A")
    else:
        print("Email : " + contact["email"])

    print("")


# Add Contact

def add_contact(name, phone, email):
    global next_id

    if not validate_phone(phone):
        print("Error: Phone must start with 07, be 10 digits, and contain digits only")
        print("Example: 0712345678")
        return

    if not validate_email(email):
        print("Error: Email must contain @ and a dot")
        return

    contact = {
        "id": next_id,
        "name": name,
        "phone": phone,
        "email": email
    }

    contacts.append(contact)
    next_id = next_id + 1

    print("Contact added successfully.")


# View Contact

def view_contact(name):
    match_name = lambda c: name.lower() in c["name"].lower()

    results = []

    for c in contacts:
        if match_name(c):
            results.append(c)

    if len(results) == 0:
        print("No contact found with that name.")
    else:
        for contact in results:
            print_contact(contact)


# Update Contact

def update_contact(contact_id, name, phone, email):

    if phone != "" and not validate_phone(phone):
        print("Error: Phone must start with 07, be 10 digits, and contain digits only")
        print("Example: 0712345678")
        return

    if email != "" and not validate_email(email):
        print("Error: Email must contain @ and a dot")
        return

    match_id = lambda c: c["id"] == contact_id

    found = None

    for c in contacts:
        if match_id(c):
            found = c
            break

    if found is None:
        print("No contact found with that ID.")
        return

    if name != "":
        found["name"] = name

    if phone != "":
        found["phone"] = phone

    if email != "":
        found["email"] = email

    print("Contact updated successfully.")


# Delete Contact

def delete_contact(contact_id):
    global contacts

    match_id = lambda c: c["id"] == contact_id

    found = None

    for c in contacts:
        if match_id(c):
            found = c
            break

    if found is None:
        print("No contact found with that ID.")
        return

    contacts.remove(found)

    print("Contact deleted.")


# List All Contacts

def list_all_contacts():

    if len(contacts) == 0:
        print("No contacts saved yet.")
    else:
        for contact in contacts:
            print_contact(contact)


# Search Contacts

def search_contacts(query):

    match_any = lambda c: (
        query.lower() in c["name"].lower() or
        query.lower() in c["phone"] or
        query.lower() in c["email"].lower()
    )

    results = []

    for c in contacts:
        if match_any(c):
            results.append(c)

    print("Search results for: " + query)
    print("")

    if len(results) == 0:
        print("No matching contacts found.")
    else:
        for contact in results:
            print_contact(contact)


# Menu After Every Operation

def menu_option():

    print("")
    print("1. Go Back to Main Menu")
    print("2. Exit")

    option = input("Choose an option (1-2): ")

    if option == "1":
        return True

    elif option == "2":
        print("You are logged out.")
        return False

    else:
        print("Invalid option. Returning to Main Menu.")
        return True


# Contact Manager Menu

while True:

    print("")
    print("Contact Manager Menu")
    print("1. Add Contact")
    print("2. View Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Search Contacts")
    print("6. List All Contacts")
    print("7. Exit")
    print("")

    choice = input("Choose an option (1-7): ")

    if choice == "1":

        name = input("Enter name  : ")
        phone = input("Enter phone : ")
        email = input("Enter email (or press Enter to skip): ")

        add_contact(name, phone, email)

        if not menu_option():
            break

    elif choice == "2":

        name = input("Enter name to view: ")

        view_contact(name)

        if not menu_option():
            break

    elif choice == "3":

        contact_id = int(input("Enter contact ID to update: "))

        name = input("New name  (press Enter to keep current): ")
        phone = input("New phone (press Enter to keep current): ")
        email = input("New email (press Enter to keep current): ")

        update_contact(contact_id, name, phone, email)

        if not menu_option():
            break

    elif choice == "4":

        contact_id = int(input("Enter contact ID to delete: "))

        confirm = input("Are you sure? (yes/no): ")

        if confirm == "yes":
            delete_contact(contact_id)
        else:
            print("Deletion cancelled.")

        if not menu_option():
            break

    elif choice == "5":

        query = input("Search by name, phone, or email: ")

        search_contacts(query)

        if not menu_option():
            break

    elif choice == "6":

        list_all_contacts()

        if not menu_option():
            break

    elif choice == "7":

        print("You are logged out.")
        break

    else:

        print("Invalid option. Please enter a number from 1 to 7.")