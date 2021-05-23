'''Decide the place of service of an employee based on their age, sex and marital status'''

__author__ = "Shakir Sadiq"

age = int(input("Enter your age: "))
sex = input("Enter your gender(M/F): ")
marital_status = input("Are you married(Y/N)?: ")
if sex == "F" or "f" and age>=20 and age<=60:
    print("you will work in urban areas only")
elif sex == "M" or "m" and age>40 and age<=60:
    print("You will work in urban areas only")
elif sex == "M" or "m" and age>=20 and age<=40:
    print("You can work anywhere")	
else:
    print("ERROR")
	