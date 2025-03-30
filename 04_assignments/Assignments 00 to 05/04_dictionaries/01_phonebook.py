def phonebook():
    contacts = {}  # Dictionary to store names and phone numbers

    while True:
        print("\nPhonebook Menu:")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. View All Contacts")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter contact name: ")
            number = input("Enter phone number: ")
            contacts[name] = number
            print(f"Contact {name} added successfully!")

        elif choice == "2":
            name = input("Enter the name to search: ")
            if name in contacts:
                print(f"{name}'s number: {contacts[name]}")
            else:
                print(f"{name} not found in phonebook.")

        elif choice == "3":
            if contacts:
                print("\nPhonebook Contacts:")
                for name, number in contacts.items():
                    print(f"{name}: {number}")
            else:
                print("Phonebook is empty.")

        elif choice == "4":
            name = input("Enter the name to delete: ")
            if name in contacts:
                del contacts[name]
                print(f"Deleted {name} from phonebook.")
            else:
                print(f"{name} not found in phonebook.")

        elif choice == "5":
            print("Exiting phonebook. Goodbye!")
            break

        else:
            print("Invalid option! Please choose again.")

# Run the phonebook
phonebook()
