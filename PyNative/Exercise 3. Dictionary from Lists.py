             #PyNative: Dictionary

#Exercise 3: Dictionary from Lists


#Given

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

# Use zip() to pair each key with its corresponding value
# Example: ('Ten', 10), ('Twenty', 20), ('Thirty', 30)
paired_items = zip(keys, values)

# Convert the paired items into a dictionary using dict()
my_dict = dict(paired_items)

# Print the final dictionary
print(my_dict)

