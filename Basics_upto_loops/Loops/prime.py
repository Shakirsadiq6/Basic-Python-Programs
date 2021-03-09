'''print all prime numbers from 1 to 300'''

FIRST = 1  #first number
LAST = 300 #last number
for num in range(FIRST,LAST+1):
    if num > 1: #Prime number starts from 2 and negative numbers are not prime.
        for i in range(2,num):
            if(num%i) == 0:
                break
        else:
            print(num)
			