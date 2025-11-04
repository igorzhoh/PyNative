"""Write Python code to iterate through the first 10 numbers and, in each iteration, print the sum of the current and previous number.

Expected Output:

Printing current and previous number sum in a range(10)
Current Number 0 Previous Number  0  Sum:  0
Current Number 1 Previous Number  0  Sum:  1
Current Number 2 Previous Number  1  Sum:  3
Current Number 3 Previous Number  2  Sum:  5
Current Number 4 Previous Number  3  Sum:  7
Current Number 5 Previous Number  4  Sum:  9
Current Number 6 Previous Number  5  Sum:  11
Current Number 7 Previous Number  6  Sum:  13
Current Number 8 Previous Number  7  Sum:  15
Current Number 9 Previous Number  8  Sum:  17"""

print("Printing current and previous number sum in a range(10)")

previous_num = 0

for i in range(10):
    sum = i + previous_num
    print("Current Number", i, "Previous Number", previous_num, "Sum:", sum)
    previous_num = i

#Explanation
"""previous_num = 0 — initially, the previous number is set to 0.

for i in range(10) — the loop iterates through numbers from 0 to 9.

sum = i + previous_num — in each iteration, the program calculates the sum of the current and the previous number.

previous_num = i — before moving to the next iteration, we store the current number as the previous one."""
