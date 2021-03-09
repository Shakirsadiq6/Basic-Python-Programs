'''WAP to find the difference between the sum of squares of
first 100 natural numbers and the square of the sum.'''

def squaresum(squarenumber):
    '''function to find sum of squares'''
    squaresum = 0
    for i in range(1, squarenumber+1):
        squaresum = squaresum + (i * i)
    return squaresum
squarenumber = 100
print("\nThe sum of squares of first 100 natural numbers: ",end="")
print(squaresum(squarenumber))
def summ(number):
    '''function to find square of the sum of the first ten natural numbers'''
    summ = 0
    for i in range(1, number+1):
        summ = summ + i
    return summ
number = 100
print("The square of the sum of first 100 natural numbers: ",end="")
print(summ(number)**2)
difference = (summ(number)**2) - (squaresum(squarenumber))
print("\nThe difference is ",end="")
print(difference)
