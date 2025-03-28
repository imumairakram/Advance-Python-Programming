contacts: dict = {}

while True:
    print("Welcome to the contact book")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Edit Contact")
    print("4. Delete Contact")
    print("5. Search Contact")
    print("6. Exit")
    
    choice = input("Enter your choice: ")

    if choice == "1":
        contactname = input("Enter contact name: ")
        contactnumber = input("Enter contact number: ")
        contacts[contactname] = contactnumber

    elif choice == "2":
        print("Contacts")
        for i in contacts:
            print(f"{i} : {contacts[i]}")

    elif choice == "3":
        contactname = input("Enter the contact name: ")
        if contactname in contacts:
            new_contactnumber = input("Enter new contact number: ")
            contacts[contactname] = new_contactnumber
            print(f"{contactname} updated successfully.")
        else:
            print("Contact not found.")
        
    elif choice == "4":
        contactname = input("Enter the contact name: ")
        if contactname in contacts:
            del contacts[contactname]
            print(f"{contactname} deleted successfully.")
        else:
            print("Contact not found.")
    
    elif choice == "5":
        contactname = input("Enter the contact name: ")
        if contactname in contacts:
            print(f"{contactname} : {contacts[contactname]}")
        else:
            print("Contact not found.")

    elif choice == "6":
        print("You exited from the contact book.")
        break
    
    else:
        print("Invalid choice. Please try again.")
