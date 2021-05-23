'''WAP for smallest positive number that is evenly divisible by all of the numbers from 1-20'''

__author__ = "Shakir Sadiq"

def gcd(first,second):
    '''Greatest common divisor'''
    return second and gcd(second, first%second) or first
def lcm(first,second):
    '''Least common multiply'''
    return first*second / gcd(first,second)
NUMBER = 1
for i in range(1, 21): #range from 1-21 as it won't take the extreme right value
    NUMBER = lcm(NUMBER, i)
print("\nThe smallest positive number that is evenly divisible by all of the numbers from 1-20: ",end="")
print(NUMBER)
