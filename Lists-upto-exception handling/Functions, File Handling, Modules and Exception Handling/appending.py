'''Program to append any input text at the end of a file.
Find size of a given file before and after appending content'''

__author__ = "Shakir Sadiq"

import os
try:
    myfile = open("file.txt","r")
    print(myfile.read())
    file_size_before = os.path.getsize("C:\\Users\\Shakir\\OneDrive\\Desktop\\Py\\Assignment5-Functions, File Handling, Modules\\file.txt")
    print("The size of the file before appending=",file_size_before)
    open_file = open("file.txt","a")
    append_file = open_file.write("\nPython is used in web development.")
    open_file.close()
    print()
    mynewfile = open("file.txt","r")
    print(mynewfile.read())
    file_size_after = os.path.getsize("C:\\Users\\Shakir\\OneDrive\\Desktop\\Py\\Assignment5-Functions, File Handling, Modules\\file.txt")
    print("The size of the file after appending=",file_size_after)
except FileNotFoundError:
    print("File not found.")
