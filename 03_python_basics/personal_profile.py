name = input("Name: ")
age = int(input("Age: "))
height = float(input("Height in meters: "))
is_student = input("Are you a student? (yes/no): ").lower() == "yes"

print("\n=== PROFILE ===")
print("Name:", name, type(name))
print("Age:", age, type(age))
print("Height:", height, type(height))
print("Student:", is_student, type(is_student))
