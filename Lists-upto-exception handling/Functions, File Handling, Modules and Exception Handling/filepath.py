'''The location of the file within the file system'''

__author__ = "Shakir Sadiq"

import os
try:
    file_abs_path = os.path.abspath('file.txt')
    print(file_abs_path)
except FileNotFoundError:
    print("File not found.")
