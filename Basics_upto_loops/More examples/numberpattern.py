'''Print the following pattern
    1010101
	 10101
	  101
	   1    '''

__author__ = "Shakir Sadiq"

COLUMN=7
ROWS=0
SPACE=3
while (COLUMN>=0 and SPACE>=0):
    a=(" "*ROWS+"10"*SPACE+"1"+" "*ROWS)
    print(a)
    SPACE=SPACE-1
    COLUMN=COLUMN-2
    ROWS=ROWS+1
