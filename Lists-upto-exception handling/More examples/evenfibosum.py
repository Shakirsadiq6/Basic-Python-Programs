''' Wap to print sum of even numbers of fibonacci series upto 4 million'''

__author__ = "Shakir Sadiq"

def evenfibo(number):
    '''function for even fibonacci series'''
    first = 1
    second = 1
    total = 0
    while first <= number:
        if first % 2 == 0:
            total += first
        first, second = second, first+second
    print(total)
number = 4000000
print("\nThe sum of even valued fibonacci terms upto 4 million: ",end="")
evenfibo(number)
