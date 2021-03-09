'''print out all Armstrong numbers between1 and 500'''

FIRST = 1  #first number
LAST = 500 #last number
for number in range(FIRST,LAST):
    SUM = 0
    temp = number   #temporary saves the value of the number
    while temp > 0: #while loop for finding the cube of each digit
        digit = temp % 10
        SUM += digit ** 3
        temp //= 10
    if number == SUM:
        print(number)
		