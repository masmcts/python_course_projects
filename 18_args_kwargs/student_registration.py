def register_student(name, *courses, **details):
    print("\n=== STUDENT ===")
    print("Name:", name)

    print("\nCourses:")
    for course in courses:
        print("-", course)

    print("\nDetails:")
    for key, value in details.items():
        print(f"{key}: {value}")

courses = ["Python", "Database", "Web Development"]
details = {
    "age": 20,
    "city": "Hatay",
    "department": "Computer Engineering"
}

register_student("Ali", *courses, **details)
