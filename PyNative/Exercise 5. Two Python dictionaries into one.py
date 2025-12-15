#Exercise 5. Merge two Python dictionaries into one


#GIven:


dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

#Expected output:

#{'Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

my_dict = {**dict1, **dict2}
print(my_dict)