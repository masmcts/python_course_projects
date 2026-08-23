# Project 1: Contact Book CLI
**Week 1 Capstone — Topics: Basics, Conditionals, Sequences, Strings, Iteration, Dictionaries, Functions**

## Goal
Build a command-line contact book where a user can add, search, list, and delete
contacts. Each contact is stored as a dictionary, and all contacts live in a list.

## What You'll Practice
- Lists and dictionaries (storing structured data)
- String methods (cleaning and validating input)
- Loops (menu that keeps running until the user quits)
- Conditionals (validating input, matching menu choices)
- Functions (one function per action, with default arguments)

## Requirements

Your program should:

1. Store contacts as a **list of dictionaries**. Each contact dict has:
   `{"name": str, "phone": str, "email": str}`
2. Show a menu in a loop:
   ```
   1. Add contact
   2. Search contact
   3. List all contacts
   4. Delete contact
   5. Quit
   ```
3. **Add contact**: ask for name, phone, email. Validate that:
   - the phone contains only digits (use `str.isdigit()` after removing spaces/dashes)
   - the email contains an `@` and a `.`
   If validation fails, show an error and ask again (or skip — your choice).
4. **Search contact**: ask for a name (or partial name) and print any contacts
   whose name *contains* that text (case-insensitive — use `.lower()`).
5. **List all contacts**: print every contact, nicely formatted.
6. **Delete contact**: ask for a name, remove the matching contact from the list.
7. **Quit**: exit the loop and print a goodbye message.

## Step-by-Step Guide

### Step 1 — Set up storage
```python
contacts = []
```

### Step 2 — Write the add function
```python
def add_contact(contacts, name, phone, email):
    ...
    contacts.append({"name": name, "phone": phone, "email": email})
```
Give `phone` and `email` default values (e.g. `""`) so the function can be
called with just a name if you want to test it quickly.

### Step 3 — Write validation helpers
Write small functions:
```python
def is_valid_phone(phone):
    cleaned = phone.replace("-", "").replace(" ", "")
    return cleaned.isdigit()

def is_valid_email(email):
    return "@" in email and "." in email
```

### Step 4 — Write search, list, and delete functions
Each should take `contacts` as a parameter and either return or print results.
Use a `for` loop with an `if` condition to filter.

### Step 5 — Build the menu loop
```python
while True:
    print(MENU_TEXT)
    choice = input("Choose an option: ")
    if choice == "1":
        ...
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid option, try again.")
```

## Stretch Goals (optional)
- Prevent duplicate contacts (same name + phone).
- Sort the contact list alphabetically before listing.
- Let the user edit an existing contact instead of deleting and re-adding.

## Testing Checklist
- [ ] Adding a contact with a bad phone number shows an error
- [ ] Searching is case-insensitive and matches partial names
- [ ] Deleting a name that doesn't exist doesn't crash the program
- [ ] Choosing an invalid menu number doesn't crash the program
- [ ] Quitting exits cleanly
