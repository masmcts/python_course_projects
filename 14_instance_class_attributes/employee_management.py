class Employee:
    company = "ABC Company"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

employee1 = Employee("Ali", 50000)
employee2 = Employee("Ayse", 60000)

print(employee1.company)
print(employee2.company)

employee1.company = "Ali's Company"  # Attribute shadowing
print("\nAfter shadowing:")
print(employee1.company)
print(employee2.company)
print(Employee.company)
