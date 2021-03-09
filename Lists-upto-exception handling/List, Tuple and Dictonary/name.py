'''Return names exists in the list. If you insert any name into the list.
It should return with other names automatically'''
name = ['harry','ron']
print("list of names:", name)
for i in range(0,5):
    i = input("Enter a name: ")
    if i not in name:
        name.append(i)
        print(name)
    else:
        print(name)
