             #PyNative: Dictionary

#Exercise 2: Perform dictionary operations


#Given:

my_dict = {'name': 'Alice', 'age': 35, 'city': 'New York', 'profession': 'Doctor'}
print("Originaly dictionary:", my_dict)


# Remove the key 'profession'

del my_dict['profession']
print("updated dictionary after removing 'profession' :", my_dict)


# Print all key–value pairs
print("printing all key-value pairs;")
for key, value in my_dict.items():
	print(f"{key}: {value}")


# Check if 'age' exists

print("Does 'age' exist?", 'age' in my_dict)

