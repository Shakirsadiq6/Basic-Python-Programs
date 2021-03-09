'''The largest prime factor of the number 600851475143'''

import math
try:
    def primefactor(number):
        '''function to calculate largest prime factor the number'''
        while number % 2 == 0:
            max_prime = 2
            number /= 1
        for i in range(3, int(math.sqrt(number)) + 1, 2):
            while number % i == 0:
                max_prime = i
                number = number / i
        if number > 2:
            max_prime = number
        return int(max_prime)
    number = 600851475143
    print("\nThe largest prime factor of 600851475143: ",end="")
    print(primefactor(number))
except ValueError:
    print("It is not a valid number")
