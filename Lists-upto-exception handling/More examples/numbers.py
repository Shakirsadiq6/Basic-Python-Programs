'''WAP for calculating how many letters would be
used to write all the numbers from 1 to 1000 in words'''

__author__ = "Shakir Sadiq"

def lettersused():
    '''function for calculating the total letters used'''
    one_to_ten=(0,3,3,5,4,4,3,5,5,4) #1,2,3,4,...
    ten_to_ninety=(0,3,6,6,5,5,5,7,6,6) #10,20,30,40,...
    eleven_to_nineteen=(0,6,6,8,8,7,7,9,8,8) #11,12,13,14,...
    rest_numbers=(7,10,11) #hundered, hundered and, one thousand.
    one_to_ninety_nine = (sum(one_to_ten)*9 + ten_to_ninety[1] + sum(eleven_to_nineteen) + sum(ten_to_ninety[2:])*10)*10
    hundered_to_nine_hundered = rest_numbers[0]*9 + rest_numbers[1]*99*9 + sum(one_to_ten)*100
    letters = one_to_ninety_nine + hundered_to_nine_hundered + rest_numbers[2]
    return letters
print("\nLetters used to write all the numbers from 1 to 100 in words: ",end="")
print(lettersused())
