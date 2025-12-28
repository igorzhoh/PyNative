# OOP Exercise 3
# Create a child class Bus that will inherit all of the variables and methods of the Vehicle class

# Given:

class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage


class Bus(Vehicle):
    pass


School_bus = Bus("School Volvo", 180, 12)
print("Vehicle Name:", School_bus.name, "Speed:", School_bus.max_speed, "Mileage:", School_bus.mileage)


#Exercise:
# Create a child class Car that inherits from the Vehicle class.
#The Vehicle class has the following attributes:
#name
# max_speed
# mileage
#
# The Car class should:
# Inherit all attributes from the Vehicle class
# Add a new attribute called doors
# Implement a method show_info() that displays all vehicle details
# Create an object of the Car class and display its information.

class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage


class Car(Vehicle):
    def __init__(self, name, max_speed, mileage, doors):
        super().__init__(name, max_speed, mileage)
        self.doors = doors

    def show_info(self):
        print(
            f"Vehicle Name: {self.name} "
            f"Speed: {self.max_speed} "
            f"Mileage: {self.mileage} "
            f"Doors: {self.doors}"
        )


car = Car("Toyota Corolla", 190, 40000, 4)
car.show_info()

