'''Pythagorean triplet for which a+b+c = 1000. WAP to find the product abc'''

try:
    def pythagorean(SUMM):
        '''function for pythagorean triplet SUMM'''
        for a in range(1,334): #334 is SUMM/3
            a += 1
            for b in range(1,501): #501 is SUMM/2
                b += 1
                c = SUMM - a - b
                if a*a + b*b == c*c:
                    print("\nThe product of a,b,c: ",end="")
                    print(a*b*c)
    SUMM = 1000
    pythagorean(SUMM)
#pylint rating below 7 because variables does not have snake-case naming style.
except ValueError:
    print("It is an invalid number")
