''' WAP to print name as abbreviations except the last name'''

__author__ = "Shakir Sadiq"

user = input("Please enter your name: ")
names = user.split()

for i in range(0, len(names)):
    if i < len(names) - 1:
        print(names[i][0], end=" ") 
    else:
        print(names[i])