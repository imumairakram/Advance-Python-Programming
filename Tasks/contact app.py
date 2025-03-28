contacts : dict = {}

while True:
    print("Welcone to the contact book")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Edit Contact")
    print("4. Delete Contact")
    print("5. Exit")
    
    choice = input("Enter your choice: ")

    if choice == "1":
        contactname = input("Enter contact name: ")
        contactnumber = input("Enter contact number: ")
        contacts[contactname] = contactnumber

    elif choice == "2":
        print ("Contacts")
        for i in contacts:
            print(f"{i} : {contacts[i]}")

    elif choice == "3":
        contactname = input("Enter the contact name: ")
        if contactname in contacts:
            new_contactnumber = input("Enter new contact number: ")
            contacts[contactname] = new_contactnumber
            print(f"{contactname} created successfully.")
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
        print("You Exited from the contact book.")
        break
    
    else:
        print("Please try again.")
