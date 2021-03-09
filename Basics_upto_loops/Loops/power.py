'''program to find the value of one number raised to the power of another'''

number1 = int(input("Enter the value of the number="))
number2 = int(input("Enter the power of the number="))
POWER = 1
for i in range(1, number2+1):
    POWER *= number1
print(number1, "raised to power", number2, "is", POWER)
