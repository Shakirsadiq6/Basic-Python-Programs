'''Write a Function to solve a polynomial equation.'''

__author__ = "Shakir Sadiq"

def polynomial(terms,value_of_x):
    '''function for evaluating a polynomial.'''
    result = 0
    for coefficient in terms:
        result = value_of_x * result + coefficient
    return result
try:
    value_of_x = int(input("Enter the value of x:"))
    first_term = int(input("Enter the value of first term:"))
    second_term = int(input("Enter the value of second term:"))
    third_term = int(input("Enter the value of third term:"))
    #for 3 or more degree terms just make more user inputs for each term.
    print("The answer of the polynomial:")
    print(polynomial((first_term,second_term,third_term), value_of_x))
except ValueError:
    print("Enter a valid number!")
