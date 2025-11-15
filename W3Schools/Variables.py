# Exercise

# name = "Ihor"
# print("Hello, " + name + "!")


# Exercise

x = 11
y = 46

# print("Addition:", x + y)
# print("Subtraction:", x - y)
# print("Multiplication:", x * y)
# print("Division:", x / y)



           #Global Variables

# Exercise

#
# x = 101  # global
#
# def show():
#     x = 55  # local
#     print("Inside function:", x)
#
# show()
# print("Outside function:", x)
#

# Exercise

# counter = 0  # global variables
#
# def increase():
#     global counter  # change global
#     counter += 1
#     print("Inside function:", counter)
#
# increase()
# increase()
# increase()
# print("Outside function:", counter)


# Exercise

# a = 100  # global
#
# def function():
#     b = 50  # локальна
#     print("Inside function:")
#     print("a =", a)  # global
#     print("b =", b)  # local
#
# function()
# print("Outside function:")
# print("a =", a)

# Exercise

total = 0  # global

def add(a, b):
    result = a + b  # local
    global total
    total += result  # змінюємо глобальну
    print("Result inside function:", result)
    print("Total so far:", total)

add(2, 3)
add(4, 5)
print("Final total:", total)

