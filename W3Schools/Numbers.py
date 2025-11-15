           # Numbers


# Exercise


# Numeric types
a = 5                # integer
b = 3.7              # float
c = 2 + 4j           # complex number

# Convert between numeric types
to_float = float(a)      # convert int -> float
to_int = int(b)          # convert float -> int (drops decimal part)
to_complex = complex(a)  # convert int -> complex (imaginary part = 0)

print("a (int) =", a, "-> to_float (float) =", to_float)
print("b (float) =", b, "-> to_int (int) =", to_int)
print("a (int) =", a, "-> to_complex (complex) =", to_complex)
print()



# Strings and numeric conversions

num_str = str(a)         # convert int -> str
float_str = str(b)       # convert float -> str
complex_str = str(c)     # complex -> str (string representation)

text = "123"
int_from_str = int(text)     # "123" -> 123 (int)
float_from_str = float(text) # "123" -> 123.0 (float)

print("num_str:", num_str, "type:", type(num_str))
print("int_from_str:", int_from_str, "type:", type(int_from_str))
print("float_from_str:", float_from_str, "type:", type(float_from_str))
print()


# Boolean conversions

x = 0
y = 5
bool_x = bool(x)   # 0 -> False
bool_y = bool(y)   # non-zero -> True
bool_empty = bool("")  # empty string -> False
bool_nonempty = bool("hello") # non-empty string -> True


print("bool(0) =", bool_x)
print("bool(5) =", bool_y)
print("bool('') =", bool_empty)
print("bool('hello') =", bool_nonempty)
print()



# Collections: list, tuple, set
numbers = [1, 2, 3]              # list
numbers_tuple = tuple(numbers)   # list -> tuple
numbers_set = set(numbers)       # list -> set (unique values)


print("list:", numbers, type(numbers))
print("tuple:", numbers_tuple, type(numbers_tuple))
print("set:", numbers_set, type(numbers_set))
print()


# Dictionary keys/values -> lists
student = {"name": "Ihor", "age": 19, "city": "Kyiv"}

keys_list = list(student.keys())     # dict_keys -> list
values_list = list(student.values()) # dict_values -> list
items_list = list(student.items())   # dict_items -> list of tuples


print("keys_list:", keys_list)
print("values_list:", values_list)
print("items_list:", items_list)
print()

