from pathlib import Path
import json

FILE = Path(__file__).with_name("tasks.json")

def load_tasks():
    try:
        with open(FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(FILE, "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=2)

tasks = load_tasks()

while True:
    print("\n1 Add  2 Show  3 Complete  0 Exit")
    choice = input("Choice: ")

    if choice == "1":
        tasks.append({"task": input("Task: "), "done": False})
        save_tasks(tasks)
    elif choice == "2":
        for i, task in enumerate(tasks, start=1):
            status = "Done" if task["done"] else "Pending"
            print(i, task["task"], "-", status)
    elif choice == "3":
        try:
            index = int(input("Task number: ")) - 1
            tasks[index]["done"] = True
            save_tasks(tasks)
        except (ValueError, IndexError):
            print("Invalid task number.")
    elif choice == "0":
        break
