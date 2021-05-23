'''program that prompts students for their percentage'''

__author__ = "Shakir Sadiq"

percentage = int(input('Enter the percentage of the student='))
if percentage>=90:
    print('The grade of the student is A')
elif percentage>=80:
    print('The grade of the student is B')
elif percentage>=70:
    print('The grade of the student is C')
elif percentage>=60:
    print('The grade of the student is D')
else:
    print('The grade of the student is F')
	