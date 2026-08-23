class Animal:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def introduce(self):
        print(f"{self.name} is {self.age} years old and {self.color}.")

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

    def make_sound(self):
        print(f"{self.name} makes a sound.")

animal = Animal("Milo", 3, "Brown")
animal.introduce()
animal.eat()
animal.sleep()
animal.make_sound()
