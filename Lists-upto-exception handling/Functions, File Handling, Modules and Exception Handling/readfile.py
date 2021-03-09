'''Program to read a file and display contents with its line numbers.'''

try:
    with open("file.txt") as open_file:
        for line_number, lines in enumerate(open_file, 1):
            print(line_number,":",lines)
except FileNotFoundError:
    print("File not found.")
