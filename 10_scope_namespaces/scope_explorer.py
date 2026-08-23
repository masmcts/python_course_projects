message = "Global"

def outer():
    message = "Enclosing"

    def inner():
        message = "Local"
        print("Inner:", message)

    inner()
    print("Outer:", message)

outer()
print("Global:", message)
print("Built-in example:", len([1, 2, 3]))
