# Task 1
# Create variables
a = "25"     # str
b = 3.8      # float
c = 0        # int

# Convert (casting)
a_int = int(a)        # str -> int
b_int = int(b)        # float -> int
c_bool = bool(c)      # int -> bool

print("a_int:", a_int, "type:", type(a_int))
print("b_int:", b_int, "type:", type(b_int))
print("c_bool:", c_bool, "type:", type(c_bool))


# Task 2
x = "10"     # str
y = "3.5"    # str
z = "True"   # str

# Convert types
x_int = int(x)           # str -> int
y_float = float(y)       # str -> float
z_bool = bool(z)         # str -> bool (any non-empty string is True)

# Perform operations
sum_result = x_int + y_float     # int + float
print("Sum:", sum_result)

print("x_int type:", type(x_int))
print("y_float type:", type(y_float))
print("z_bool value:", z_bool)

