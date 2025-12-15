#Exercise 6. Count Character Frequencies


#Given:

string1 = 'Jessa'

#Expected Output:
#Frequencies for 'Jessa': {'J': 1, 'e': 1, 's': 2, 'a': 1}


frequencies = {} #Empty dictionary

for char in string1:
    if char in frequencies:
        frequencies[char] += 1
    else:
        frequencies[char] = 1

print(f"Frequencies for '{string1}': {frequencies}")