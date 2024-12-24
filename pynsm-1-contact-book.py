def access_to_contact_book():
    verification = input("Do you want to access the contact book?\nAnswer >> Yes or No :: ")
    if verification.lower() == "yes":
        return True
    return False

def menu_options():
    print("\nContact Book")
    print("1. Create a new contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

def create_contact(contact_lists):
    name = input("Enter name: ")
    phone = input("Add phone number: ")
    email = input("Enter email address: ")
    company = input("Enter company's name: ")
    contact = (name, phone, email, company)
    contact_lists.append(contact)
    print(f"Contact {name} added successfully.")

def view_all_contacts(contact_lists):
    if not contact_lists:
        print("No contacts available.")
    else:
        print("\nAll Contacts:")
        for contact in contact_lists:
            print(f"Name: {contact[0]}, Phone: {contact[1]}, Email: {contact[2]}, Company: {contact[3]}")

def search_contact(contact_lists):
    f_name = input("Enter the name to search: ")
    for each_contact in contact_lists:
        if f_name.lower() == each_contact[0].lower():
            print("Search Results:")
            print(f"Name: {each_contact[0]}, Phone: {each_contact[1]}, Email: {each_contact[2]}, Company: {each_contact[3]}")
            return
    print(f"No contacts found with the name '{f_name}'.")

def delete_contact(contact_lists):
    d_name = input("Enter the name of the contact to delete: ")
    for each_contact in contact_lists:
        if d_name.lower() == each_contact[0].lower():
            contact_lists.remove(each_contact)
            print(f"Contact {d_name} deleted successfully.")
            return
    print(f"No contact found with the name '{d_name}'.")

def exit_program():
    print("Exiting Contact Book. Goodbye!")

def main():
    contact_lists = []
    if access_to_contact_book():
        while True: #not to end
            menu_options()
            try:
                choice = int(input("What do you want to do? Please choose one option (1 to 5): "))
                if choice == 1:
                    create_contact(contact_lists)
                elif choice == 2:
                    view_all_contacts(contact_lists)
                elif choice == 3:
                    search_contact(contact_lists)
                elif choice == 4:
                    delete_contact(contact_lists)
                elif choice == 5:
                    exit_program()
                    break
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Please enter a valid number.")
    else:
        print("Access denied.")

if __name__ == "__main__":
    main()
