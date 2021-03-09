'''Multiplication table of any number'''

number = int(input("Enter your number= "))
for i in range(1,11):
    multiply = i*number
    print(number, "*", i, "=", multiply)
