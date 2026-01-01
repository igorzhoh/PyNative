class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"


class Bus(Vehicle):
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity)


bus = Bus("bus", 120, 15)
print(bus.seating_capacity())




#Given (Parent Class)
class Person:
    def __init__(self, name):
        self.name = name

    def greeting(self, language):
        return f"Hello, my name is {self.name}. Language: {language}"

#Expected Output
#Hello, my name is Anna. Language: English

class Teacher(Person):
    def greeting(self, language="English"):
        return super().greeting(language)


teacher = Teacher("Anna")
print(teacher.greeting())



#Problem Statement
# Create a class Employee.
# Then create a child class Manager that inherits from the Employee class.
# Requirements
#
# The Employee class should have:
# an attribute name
# an attribute salary
# a method get_info() that returns employee information
#
# The Manager class should:
# inherit from Employee
# add a new attribute department
# override the get_info() method to include the department
# Create a Manager object and print its information.


#Given (Parent Class)
#super() is used in a child class to call methods from the parent class.

class Employee:                                 #Parent class
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_info(self):
        return f"Name: {self.name}, Salary: {self.salary}"

# Expected Output (example)
# Name: John, Salary: 5000, Department: IT

class Manager(Employee):                        #Child class
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department    #new attribute added only in Manager

    def get_info(self):                         #Method overriding
        return f"{super().get_info()}, Department: {self.department}"


manager = Manager("John", 5000, "IT")
print(manager.get_info())