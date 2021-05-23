'''aggregate marks and percentage marks
obtained by a student in five different subjects'''

__author__ = "Shakir Sadiq"

english = int(input('Enter the marks of english= '))
science = int(input('Enter the marks of science= '))
maths = int(input('Enter the marks of maths= '))
computer = int(input('Enter the marks of computer= '))
history = int(input('Enter the marks of history= '))
total_marks = english+science+maths+computer+history #aggregate_marks
percentage = (total_marks/5)
print('Aggregate Marks= ',total_marks)
print('Percentage= ',percentage)
