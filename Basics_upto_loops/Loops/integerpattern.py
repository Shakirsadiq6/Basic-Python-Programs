''' Program to produce the following output:
                    1
				   2 3
				  4 5 6
				 7 8 9 10 '''

__author__ = "Shakir Sadiq"

ROWS = 4   #NUMBER of ROWS
NUMBER = 1 #Pattern will start with integer 1
SPACE = 4  #space from the extreme right side of the screen
for i in range(0, ROWS):
    for j in range(0, SPACE):
        print(end=" ")
    SPACE = SPACE-1 #decreasing the space after each iteration
    for j in range(0, i + 1):
        print("",NUMBER, end="") #printing the numbers starting with 1
        NUMBER += 1 #incrementing the value of integer by 1 after each iteration
    print("")
	