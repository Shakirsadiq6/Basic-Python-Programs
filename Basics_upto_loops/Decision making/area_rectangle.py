'''program to find whether the area of the rectangle is greater than its perimeter'''

length = int(input('Enter the length of the rectangle:'))
breadth = int(input('Enter the breadth of the rectangle:'))
area = length*breadth
perimeter = 2*(length+breadth)
print('Area of rectangle=',area)
print('Perimeter of rectangle=',perimeter)
if area>perimeter:
    print('The area of the rectangle is greater than its perimeter.')
else:
    print('The area of the rectangle is smaller than its perimeter.')
	