'''print the distance between cities in meters, feet, inches and centimeters'''

__author__ = "Shakir Sadiq"

kilometer = float(input('Enter distance between cities(in km)= '))
meter = kilometer*1000
centimeter = kilometer*100000
feet = kilometer*1000*100*0.0328
inch = kilometer*1000*100*0.3937
print('Distance in meter= ',meter)
print('Distance in centimeter= ',centimeter)
print('Distance in feet= ',feet)
print('Distance in inch= ',inch)
