'''Combine four lists to make two dictionaries and then combine two dictionaries into one'''

__author__ = "Shakir Sadiq"

list1 = ['milk','coffee','rice','Cheese','Cereals']
list2 = ['milk','coffee','pulses','Alcohol']
list3 = [90,80,100,70,50]
list4 = [90,80,100,750]
a = dict(zip(list1, list3))
b = dict(zip(list2, list4))
print("a=",a)
print("b=",b)
c = dict(a)
c.update(b)
for i, j in a.items():
    for x, y in b.items():
        if i == x:
            c[i]=(j+y)
print("c=",c)
