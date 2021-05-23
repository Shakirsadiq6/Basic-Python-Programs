'''program to obtain the sum of
the first and last digit of a number'''

__author__ = "Shakir Sadiq"

number = int(input('Enter the 4 digit number= '))
last_digit = number%10
first_digit = number//1000
sum = last_digit+first_digit
print('The sum of the first and the last digit of the number=', sum)
