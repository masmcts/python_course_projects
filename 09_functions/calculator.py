def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b=1):
    if b == 0:
        return "Cannot divide by zero."
    return a / b

def all_operations(a, b):
    return add(a, b), subtract(a, b), multiply(a, b)

a = float(input("First number: "))
b = float(input("Second number: "))

print("Add:", add(a, b))
print("Subtract:", subtract(a, b))
print("Multiply:", multiply(a, b))
print("Divide:", divide(a, b))
print("Multiple returns:", all_operations(a, b))
