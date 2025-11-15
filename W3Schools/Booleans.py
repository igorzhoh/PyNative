# Task

a = 5
b = 0

print("a =", a, "->", bool(a))  # True
print("b =", b, "->", bool(b))  # False

# Task

x = 10
y = 3

print("x > y:", x > y)          # True, 10 > 3
print("x == y:", x == y)        # False, 10 ≠ 3
print("x < y or x == 10:", x < y or x == 10)  # True, бо друга умова істинна
print("x < y and x == 10:", x < y and x == 10) # False, бо перша хибна


# Task:
#Напиши програму, яка:
#Запитує в користувача число.
#Перевіряє, чи це додатне число.
#Перевіряє, чи воно ціле (int).
#Виводить True або False для кожної перевірки.

num = 5.0

is_positive = num > 0
is_integer = isinstance(num, int)

print("Is positive?", is_positive)
print("Is integer?", is_integer)


# Task:

a = "Python"
b = 123
c = [1, 2, 3]
d = 4.5

# Твоя задача:
# перевір кожну змінну з допомогою isinstance() і виведи результат

print(isinstance(a, str)) 	#True
print(isinstance(b, int)) 	#True
print(isinstance(c, list)) 	#True
print(isinstance(d, float))	#True