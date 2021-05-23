'''program to reverse the number'''

__author__ = "Shakir Sadiq"

number = int(input('Enter a five digit number= '))
Reverse = 0
digit1 = number%10
Reverse = (Reverse*10)+digit1
number1 = number//10
digit2 = number1%10
Reverse = (Reverse*10)+digit2
number2 = number1//10
digit3 = number2%10
Reverse = (Reverse*10)+digit3
number3 = number2//10
digit4 = number3%10
Reverse = (Reverse*10)+digit4
number4 = number3//10
digit5 = number4%10
Reverse = (Reverse*10)+digit5
print('The reverse of the five digit number= ',Reverse)
