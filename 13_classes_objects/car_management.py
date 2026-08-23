class Car:
    vehicle_type = "Car"

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

car1 = Car("Toyota", "Corolla", 2024)
car1.color = "Red"  # Dynamic attribute

print(car1.brand)
print(car1.color)
print(isinstance(car1, Car))
print(type(car1))
