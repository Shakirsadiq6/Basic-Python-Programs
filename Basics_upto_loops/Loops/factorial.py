'''Program to find the factorial value of any number'''

number = int(input("Enter a number= "))
if number < 0:
    print("Factorial does not exist for negative number.")
else:
    FACTORIAL = 1
    for i in range(1,number+1):
        FACTORIAL = FACTORIAL*i
    print ("The factorial of",number, "is", FACTORIAL)
	