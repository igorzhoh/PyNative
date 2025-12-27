#OOP Exercise 1:
#Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.

class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage


car = Vehicle(180, 25000)

print(car.max_speed)
print(car.mileage)


# class Vehicle:
#     def __init__(self):
#         self.max_speed = 0
#         self.mileage = 0
#
#
# car = Vehicle()
# car.max_speed = 200
# car.mileage = 30000
#
# print(car.max_speed)
# print(car.mileage)


#from GPT

# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# student1 = Student("Ihor", 25)
#
# print(student1.name)
# print(student1.age)