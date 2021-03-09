'''function to determine whether the year is a leap year or not.'''

def year_function(year):
    '''function for defining a leap year'''
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
try:
    year = int(input("Enter year:"))
    if year_function(year):
        print(year,"is a Leap Year")
    else:
        print(year,"is not a Leap Year")
except ValueError:
    print("Please enter a valid year!")
