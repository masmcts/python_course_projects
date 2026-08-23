items = ["milk", "bread", "eggs"]

while True:
    print("\n1. Show  2. Add  3. Remove  4. Search  5. Slice  0. Exit")
    choice = input("Choice: ")

    if choice == "1":
        print(items)
        print("First:", items[0] if items else "None")
        print("Last:", items[-1] if items else "None")
        print("Length:", len(items))
    elif choice == "2":
        items.append(input("Item: "))
    elif choice == "3":
        item = input("Item to remove: ")
        if item in items:
            items.remove(item)
        else:
            print("Not found.")
    elif choice == "4":
        item = input("Search: ")
        print(item in items)
    elif choice == "5":
        print(items[1:3])
    elif choice == "0":
        break
