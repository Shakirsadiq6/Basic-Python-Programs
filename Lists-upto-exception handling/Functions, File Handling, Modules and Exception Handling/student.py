'''Program to read student records and display them in sorted order by name'''

read_file = open('studentrecord.txt')
contents = read_file.readlines()
contents.sort()
read_file = open('studentrecord.txt','w')
for line in contents:
    read_file.write(line)
