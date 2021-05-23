'''Create a list of subjects. Assign each subject to 5 students.
Then Make a list of toppers in each subject'''

__author__ = "Shakir Sadiq"

subjects = ['physics', 'chemistry', 'maths']
physics_marks = []
chemistry_marks = []
maths_marks = []
names = []
for i in range(0,5):
    name = input("Enter the student's name: ")
    physics = int(input("Enter your marks in physics: "))
    chemistry = int(input("Enter your marks in chemistry: "))
    maths = int(input("Enter your marks in maths: "))
    print()
    physics_marks.append(physics)
    chemistry_marks.append(chemistry)
    maths_marks.append(maths)
    names.append(name)
dict_physics = dict(zip(physics_marks,names))
print("\nThe topper of physics with marks & name as:",max([i for i in dict_physics.items()]))
dict_chemistry = dict(zip(chemistry_marks,names))
print("\nThe topper of chemistry with marks & name as:",max([i for i in dict_chemistry.items()]))
dict_maths = dict(zip(maths_marks,names))
print("\nThe topper of maths with marks & name as:",max([i for i in dict_maths.items()]))
