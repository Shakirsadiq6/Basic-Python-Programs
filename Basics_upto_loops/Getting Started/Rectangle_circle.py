'''calculate the area & perimeter of the rectangle,
and the area & circumference of the circle'''

PI = 3.14
length = float(input('Enter the length of rectangle= '))
breadth = float(input('Enter the breadth of rectangle= '))
radius = float(input('Enter the radius of circle= '))
area = length*breadth
Perimeter = 2*(length+breadth)
area_circle = PI*radius*radius
circumference = 2*PI*radius
print('Area of rectangle= ',area)
print('Perimeter of rectangle= ',Perimeter)
print('Area of circle= ',area_circle)
print('Circumference of circle= ',circumference)
