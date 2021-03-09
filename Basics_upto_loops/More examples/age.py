'''determine the youngest and oldest of 3 people'''

age1 = int(input('Enter the age of age1='))
age2 = int(input('Enter the age of age2='))
age3 = int(input('Enter the age of age3='))
if (age1<=age2 and age1<=age3):
    print('The youngest is person having age=',age1)
elif (age2<=age3 and age2<=age1):
    print('The youngest is person having age=',age2)
else:
    print('The youngest is person having age=',age3)
if (age1>=age2 and age1>=age3):
    print('The oldest is person having age=',age1)
elif (age2>=age3 and age2>=age1):
    print('The oldest is person having age=',age2)
else:
    print('The oldest is person having age=',age3)
