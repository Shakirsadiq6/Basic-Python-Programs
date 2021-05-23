'''Program to enter user name and print ASCII of each character'''

__author__ = "Shakir Sadiq"

name = input("Please Enter your name: ")
print("Your name=", name)
for i in range(len(name)):
    print("The ASCII Value of Character", (name[i], ord(name[i])))
