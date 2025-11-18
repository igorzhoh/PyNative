 # Lists

#Excercises 1

#Виведи перший і останній елемент
#Додай нове число
#Заміни другий елемент
#Видали певний елемент
#Виведи довжину списку

# Create a list
numbers = [10, 20, 30, 40, 50]

print("Original list:", numbers)

# 1. First and last elements
print("First element:", numbers[0])
print("Last element:", numbers[-1])

# 2. Add a new number
numbers.append(60)
print("After append:", numbers)

# 3. Replace the second element
numbers[1] = 99
print("After replacement:", numbers)

# 4. Remove an element
numbers.remove(30)
print("After removing 30:", numbers)

# 5. Length of the list
print("Length:", len(numbers))


#Excercises 2

#Вивести перші 3 фрукти
#Вивести список у зворотному порядку
#Перебрати всі елементи циклом і вивести їх
#Створити новий список, де будуть лише елементи зі 2 по 4


fruits = ["apple", "banana", "orange", "kiwi", "mango", "pear"]

# 1. First three fruits
print("First three:", fruits[:3])

# 2. Reverse list
print("Reversed:", fruits[::-1])

# 3. Loop through elements
print("All fruits:")
for item in fruits:
    print(item)

# 4. Slice from index 1 to 3
new_list = fruits[1:4]
print("Slice (1:4):", new_list)


#Excercises 3

#Знайти суму всіх елементів
#Знайти максимальне і мінімальне значення
#Створити новий список, який міститиме лише парні числа
#Підняти кожен елемент до квадрату (square each number)


numbers = [3, 10, 7, 8, 21, 14, 6]

# 1. Sum
total = sum(numbers)
print("Sum:", total)

# 2. Min and Max
print("Min:", min(numbers))
print("Max:", max(numbers))

# 3. Even numbers
evens = [x for x in numbers if x % 2 == 0]
print("Even numbers:", evens)

# 4. Squares
squares = [x ** 2 for x in numbers]
print("Squares:", squares)



#Excercises 4

#data = [[1, 2], [3, 4, 5], [6]]

#Вивести другий внутрішній список
#Вивести елемент «5»
#Додати число 7 у третій внутрішній список
#Знайти суму всіх чисел у всіх вкладених списках


data = [[1, 2], [3, 4, 5], [6]]

# 1. Second inner list
print("Second list:", data[1])

# 2. Number 5
print("Element 5:", data[1][2])

# 3. Add 7 to the third list
data[2].append(7)
print("After append:", data)

# 4. Sum of all numbers
total = sum(sum(inner) for inner in data)
print("Total sum:", total)


#Excercises 5

#Є список чисел.
#Перебрати список циклом
#Вивести тільки ті числа, які більші за 10
#Створити новий список, куди додати лише непарні числа
#Порахувати, скільки чисел у списку більше за 20

numbers = [5, 12, 7, 22, 9, 31, 4, 18]

# 1–2. Print numbers greater than 10
print("Numbers > 10:")
for n in numbers:
    if n > 10:
        print(n)

# 3. Create a list of odd numbers
odd_numbers = []
for n in numbers:
    if n % 2 != 0:
        odd_numbers.append(n)
print("Odd numbers:", odd_numbers)

# 4. Count numbers greater than 20
count = 0
for n in numbers:
    if n > 20:
        count += 1
print("Numbers > 20:", count)
