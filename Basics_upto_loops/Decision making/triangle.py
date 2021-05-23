'''a program to check whether a triangle is valid or not'''

__author__ = "Shakir Sadiq"

first_angle = int(input('Enter the first angle of triangle='))
second_angle = int(input('Enter the second angle of triangle='))
third_angle = int(input('Enter the third angle of triangle='))
sum_angles = first_angle+second_angle+third_angle
print('The sum of the angles=',sum_angles)
if sum_angles==180:
    print('Thus it is a Valid Triangle.')
else:
    print('Thus it is an Invalid Triangle')
	