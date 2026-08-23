students = {}

while True:
    print("\n1 Add  2 Search  3 Update  4 Delete  5 Show  0 Exit")
    choice = input("Choice: ")

    if choice == "1":
        student_id = input("ID: ")
        students[student_id] = {
            "name": input("Name: "),
            "grade": float(input("Grade: "))
        }
    elif choice == "2":
        student_id = input("ID: ")
        print(students.get(student_id, "Student not found."))
    elif choice == "3":
        student_id = input("ID: ")
        if student_id in students:
            students[student_id]["grade"] = float(input("New grade: "))
    elif choice == "4":
        student_id = input("ID: ")
        students.pop(student_id, None)
    elif choice == "5":
        for student_id, info in students.items():
            print(student_id, info)
        print("Keys:", students.keys())
        print("Values:", students.values())
    elif choice == "0":
        break
