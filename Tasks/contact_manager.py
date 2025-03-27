contacts = []

while True:
    print("\n1. Add Contact ")
    print("2. Show Contact ")
    print("3. Search Contact ")
    print("4. Delete Contact")

    userchoice = input("Enter your choice: ")

    if userchoice == "1":
        contactname = input("Enter contact name: ")
        contactnumber = input("Enter contact number: ")
        contact = f"{contactname} - {contactnumber}"
        contacts.append(contact)

    elif userchoice == "2":
        if contacts:
            for i in contacts:
                print(i)
        else:
            print("No contacts found.")

    elif userchoice == "3":
        contact_name = input("Enter the name to search: ")
        for i in contacts:
            if contact_name in i:
                print(i)

    elif userchoice == "4":
        contact_name = input("Enter the name to delete: ")
        for i in contacts:
            if contact_name in i:
                contacts.remove(i)
                print("Contact deleted.")
                break  
