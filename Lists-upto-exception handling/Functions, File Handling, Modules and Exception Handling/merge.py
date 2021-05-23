'''program to merge the content of two files, copy the
merged file to a specified location. Then split merged file.'''

__author__ = "Shakir Sadiq"

import shutil
#merging the two files
try:
    file1 = open("merge1.txt")
    file1_contents = file1.read()
    file1.close()
    file2 = open("merge2.txt")
    file2_contents = file2.read()
    file2.close()
    file3 = open("merged.txt", "w")
    file3.write(f"{file1_contents}\n{file2_contents}")
    file3.close()
    print("Files merged!")
    #copying the newfile to other destination
    files = ['merged.txt']
    for f in files:
        #destination of the copied file
        shutil.copy(f, "C:/Users/Shakir/OneDrive/Desktop")
    print("New file copied to specified location!")
    #splitting the file into two
    split_lines = 2
    output = 'split'
    input = open('merged.txt', 'r')
    count = 0
    output_file_name = 1
    destination = None
    for line in input:
        if count % split_lines == 0:
            if destination:
                destination.close()
            destination = open(output + str(output_file_name) + '.txt', 'w')
            output_file_name += 1
        destination.write(line)
        count += 1
    print("File splitted into two new files!")
except FileNotFoundError:
    print("Files not found!")
