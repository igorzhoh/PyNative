 #Operators


a = 63
b = 42

print("\n    Arithmetic operators    ")
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} % {b} = {a % b}")
print(f"{a} ** {b} = {a ** b}")

print("\n    Comparison operators    ")
print(f"{a} > {b}: {a > b}")
print(f"{a} < {b}: {a < b}")
print(f"{a} == {b}: {a == b}")
print(f"{a} != {b}: {a != b}")

print("\n    Logical operators    ")
print(f"(a > b) and (a > 0): {(a > b) and (a > 0)}")
print(f"(a < b) or (b > 0): {(a < b) or (b > 0)}")
print(f"not(a == b): {not(a == b)}")

print("\n    Assignment operators    ")
x = a
print(f"First x = {x}")
x += b
print(f"x += b -> {x}")
x *= 2
print(f"x *= 2 -> {x}")
x -= 10
print(f"x -= 10 -> {x}")

print("\n    Operatoe in    ")
text = "Hello Python"
print(f"'P' in '{text}': {'P' in text}")
print(f"'z' not in '{text}': {'z' not in text}")

print("\n    Operator is    ")
n1 = 5
n2 = 5
print(f"n1 is n2: {n1 is n2}")
print(f"n1 == n2: {n1 == n2}")  # порівняння значень

