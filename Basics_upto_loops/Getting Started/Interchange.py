'''program to interchange the contents of C and D'''

__author__ = "Shakir Sadiq"

c = int(input('Enter first number(C)= '))
d = int(input('Enter second number(D)= '))
c = c + d
d = c - d
c = c - d
print('After interchange first number(C)= ',c)
print('After interchange second number(D)= ',d)
