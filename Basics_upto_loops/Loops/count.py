'''program to enter the numbers till the user wants and at the end
it displays the count of positive, negative and zeros entered'''

__author__ = "Shakir Sadiq"

number = int(input("Number of times you want to enter the integer="))
NEGATIVE = 0
POSITIVE = 0
ZERO = 0
for i in range(0,number):
    value = int(input("Enter the values=")) #stores all values entered
    if value>0:
        POSITIVE = POSITIVE+1
    elif value<0:
        NEGATIVE = NEGATIVE+1
    else:
        ZERO = ZERO+1
print("Count of positive numbers=", POSITIVE)
print("Count of negative numbers=", NEGATIVE)
print("Count of Zeroes=", ZERO)
