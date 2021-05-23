'''WAP to print absolute value of a nummber entered by user'''

__author__ = "Shakir Sadiq"

number = int(input("Enter a number="))
if number<0:
    print(number*-1)
elif number>0:
    print(number)
