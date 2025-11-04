#Exercise1

"""x = "awesome"
y = "easy"
z = "powerful"

def myfunc():
    global x, y, z
    x = "fantastic"
    y = "interesting"
    z = "popular"

myfunc()

print("Python is " + x)
print("Learning Python is " + y)
print("And Python is very " + z)"""


#Exercise2

language = "Python"
x = "awesome"
y = "simple"

def myfunc():
    x = "fantastic"   # local variable
    y = "powerful"    # local variable
    print("Inside the function:")
    print(language + " is " + x)
    print("Learning " + language + " is " + y)

print("Before calling the function:")
print("Python is " + x)
print("Python is " + y)
print()

myfunc()

print()
print("After calling the function:")
print("Python is " + x)
print("Python is " + y)

