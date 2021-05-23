'''Program to read a file and print number of words, alphabets,
numbers, special characters and white spaces using functions'''

__author__ = "Shakir Sadiq"

def count_function(file):
    '''function for counting characters in a text file.'''
    white_space = 0
    digits = 0
    alphabets = 0
    special_characters = 0
    while True:
        file_content = file.read(1)
        if file_content.isspace(): 
            white_space += 1
        if file_content.isdigit():
            digits += 1
        if file_content.isalpha():
            alphabets += 1
        if file_content in ['!','@','#','$','%','^','&','*','.','/',';',':','?',',']:
            special_characters += 1
        if not file_content:
            break
    file.close()
    return alphabets, digits, special_characters, white_space
try:
    file = open("count.txt", "r")
    data = file.read()
    words = data.split()
    file.close()
    print("Number of words in text file:",len(words))
    file = open("count.txt", "r")
    alphabets, digits, special_characters, white_space = count_function(file)
    print("Number of alphabets in text file:",alphabets)
    print("Number of digits in text file:",digits)
    print("Number of special characters in text file:",special_characters)
    print("Number of white spaces in text file:",white_space)
except FileNotFoundError:
    print("File not found.")
