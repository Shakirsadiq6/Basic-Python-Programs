''' WAP to print odd numbers fibonacci series upto 4 million'''

__author__ = "Shakir Sadiq"

TOTAL_TERMS = 4000000
NUMBER1 = 0
NUMBER2 = 1
SUM = 0
COUNT = 1
print("Odd numbers of Fibonacci Series: ", end = " ")
print()
while(COUNT <= TOTAL_TERMS):
    COUNT += 1
    NUMBER1 = NUMBER2
    NUMBER2 = SUM
    SUM = NUMBER1 + NUMBER2
    if SUM%2 != 0:
        print(SUM)