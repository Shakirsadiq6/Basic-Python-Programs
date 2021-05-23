''' function which receives a float and an int from main(), find the product
of these two and returns the product which is printed through main().'''

__author__ = "Shakir Sadiq"

def product(float_number, integer_number):
    '''function for multiplication of two numbers'''
    product = float_number*integer_number
    return product
def main():
    '''main function'''
    try:
        number1 = float(input("Enter a float:"))
        number2 = int(input("Enter an integer :"))
        multiply = product(number1,number2)
        print("\nThe product is",multiply)
    except ValueError:
        print("Enter a valid number!")
main()
