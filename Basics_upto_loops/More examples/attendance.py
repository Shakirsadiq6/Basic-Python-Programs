'''program to determine the attendance if less than 75% student is not allowed to sit in exam. Only medical cause students'''

__author__ = "Shakir Sadiq"

number_of_classes_held = int(input("Total number of classes held:"))
number_of_classes_attended = int(input("Total number of classes attended:"))
percentage = (number_of_classes_attended/number_of_classes_held)*100
if percentage>=75:
    print("You are allowed to sit in the exam")
else:
    medical_cause = input("Do you have any medical cause(Y/N)? ")
    if medical_cause == 'Y' or 'y':
        print("You are allowed to sit in the exam")
    else:
        print("You are not allowed to sit in the exam")
