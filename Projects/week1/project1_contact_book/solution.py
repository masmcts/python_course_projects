"""
Project 1: Contact Book CLI - SOLUTION
Week 1 Capstone: Basics, Conditionals, Sequences, Strings, Iteration, Dictionaries, Functions
"""

MENU_TEXT = """
==== Contact Book ====
1. Add contact
2. Search contact
3. List all contacts
4. Delete contact
5. Quit
"""


def is_valid_phone(phone):
    """Return True if phone contains only digits after removing spaces/dashes."""
    cleaned = phone.replace("-", "").replace(" ", "")
    return cleaned.isdigit() and len(cleaned) > 0


def is_valid_email(email):
    """A very simple email check: must contain '@' and '.'."""
    return "@" in email and "." in email


def add_contact(contacts, name="", phone="", email=""):
    """Add a new contact dict to the contacts list, with basic validation."""
    if not name.strip():
        print("Name cannot be empty.")
        return

    if not is_valid_phone(phone):
        print(f"'{phone}' is not a valid phone number. Contact not added.")
        return

    if not is_valid_email(email):
        print(f"'{email}' is not a valid email. Contact not added.")
        return

    contacts.append({"name": name.strip(), "phone": phone.strip(), "email": email.strip()})
    print(f"Added contact: {name}")


def search_contacts(contacts, query):
    """Return a list of contacts whose name contains the query (case-insensitive)."""
    query = query.lower()
    return [c for c in contacts if query in c["name"].lower()]


def list_contacts(contacts):
    """Print every contact in a readable format."""
    if not contacts:
        print("No contacts saved yet.")
        return

    print(f"\n{'Name':<20}{'Phone':<15}{'Email':<25}")
    print("-" * 60)
    for c in contacts:
        print(f"{c['name']:<20}{c['phone']:<15}{c['email']:<25}")


def delete_contact(contacts, name):
    """Remove the first contact matching name (case-insensitive). Return True if removed."""
    for i, c in enumerate(contacts):
        if c["name"].lower() == name.lower():
            del contacts[i]
            print(f"Deleted contact: {c['name']}")
            return True
    print(f"No contact found named '{name}'.")
    return False


def main():
    contacts = []

    while True:
        print(MENU_TEXT)
        choice = input("Choose an option: ").strip()

        if choice == "1":
            name = input("Name: ")
            phone = input("Phone (digits only): ")
            email = input("Email: ")
            add_contact(contacts, name, phone, email)

        elif choice == "2":
            query = input("Search by name: ")
            results = search_contacts(contacts, query)
            if results:
                list_contacts(results)
            else:
                print("No matches found.")

        elif choice == "3":
            list_contacts(contacts)

        elif choice == "4":
            name = input("Name to delete: ")
            delete_contact(contacts, name)

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid option, please choose 1-5.")


if __name__ == "__main__":
    main()
