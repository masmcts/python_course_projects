"""
Project 4: Inventory Manager with Action Logging - SOLUTION
Week 2 Capstone: Scope, OOP Basics, Exceptions, File Handling, *args/**kwargs
"""

import csv

# Module-level "global" state used to demonstrate scope
action_count = 0
action_log = []


class Item:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

    def total_value(self):
        return self.quantity * self.price

    def __str__(self):
        return f"{self.name}: {self.quantity} units @ ${self.price:.2f}"


def log_action(action, *args, **kwargs):
    """
    Build a readable log entry from any combination of positional args
    and keyword args, and return it (caller decides what to do with the
    updated count -- see the scope note in the tutorial).
    """
    extra_args = " ".join(str(a) for a in args)
    extra_kwargs = " ".join(f"{k}={v}" for k, v in kwargs.items())
    entry = f"[{action}] {extra_args} {extra_kwargs}".strip()
    action_log.append(entry)
    print(f"LOG: {entry}")
    return entry


def find_item(inventory, name):
    for item in inventory:
        if item.name.lower() == name.lower():
            return item
    return None


def add_item(inventory, name, quantity, price):
    existing = find_item(inventory, name)
    if existing:
        existing.quantity += quantity
        log_action("ADD", item=name, quantity=quantity, new_total=existing.quantity)
    else:
        inventory.append(Item(name, quantity, price))
        log_action("ADD", item=name, quantity=quantity, price=price)


def remove_item(inventory, name, quantity):
    item = find_item(inventory, name)
    if not item:
        raise ValueError(f"No item named '{name}' in inventory.")
    if quantity > item.quantity:
        raise ValueError(
            f"Cannot remove {quantity} of '{name}', only {item.quantity} in stock."
        )
    item.quantity -= quantity
    log_action("REMOVE", item=name, quantity=quantity, remaining=item.quantity)


def total_inventory_value(inventory):
    return sum(item.total_value() for item in inventory)


def restock_needed(inventory, threshold=5):
    """Stretch goal: return items at or below the given threshold."""
    return [item for item in inventory if item.quantity <= threshold]


def save_inventory(inventory, filename="inventory.csv"):
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["name", "quantity", "price"])
        for item in inventory:
            writer.writerow([item.name, item.quantity, item.price])
    print(f"Saved {len(inventory)} item(s) to {filename}.")


def load_inventory(filename="inventory.csv"):
    inventory = []
    try:
        with open(filename, "r", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                inventory.append(
                    Item(row["name"], int(row["quantity"]), float(row["price"]))
                )
    except FileNotFoundError:
        print(f"No existing inventory file '{filename}' found — starting fresh.")
    return inventory


MENU_TEXT = """
==== Inventory Manager ====
1. Add item
2. Remove item
3. View inventory
4. Total inventory value
5. Low stock report
6. Save & Quit
"""


def main():
    global action_count
    inventory = load_inventory()

    while True:
        print(MENU_TEXT)
        choice = input("Choose an option: ").strip()

        if choice == "1":
            name = input("Item name: ").strip()
            try:
                quantity = int(input("Quantity: "))
                price = float(input("Price per unit: "))
                add_item(inventory, name, quantity, price)
                action_count += 1  # scope note: modifying a module-level var
            except ValueError:
                print("Please enter valid numbers for quantity and price.")

        elif choice == "2":
            name = input("Item name: ").strip()
            try:
                quantity = int(input("Quantity to remove: "))
                remove_item(inventory, name, quantity)
                action_count += 1
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "3":
            if not inventory:
                print("Inventory is empty.")
            for item in inventory:
                print(item)

        elif choice == "4":
            print(f"Total inventory value: ${total_inventory_value(inventory):.2f}")

        elif choice == "5":
            low = restock_needed(inventory)
            if not low:
                print("No items are low on stock.")
            for item in low:
                print(f"LOW STOCK: {item}")

        elif choice == "6":
            save_inventory(inventory)
            print(f"Total actions this session: {action_count}")
            print("Goodbye!")
            break

        else:
            print("Invalid option, please choose 1-6.")


if __name__ == "__main__":
    main()
