'''Write a function to obtain the prime factors of this number'''

__author__ = "Shakir Sadiq"

def primefactors(number):
    '''function for prime factors of a number'''
    while number%2 == 0:
        print(2)
        number = number/2
    for i in range(3,int(number**2)+1,2):
        while number%i== 0:
            print(i)
            number = number/i
    if number>2:
        print(number)
try:
    number = int(input("Enter any number:"))
    primefactors(number) #function call
except ValueError:
    print("Enter a valid number.")
