'''print pyramid of first 10 english alphabets'''

ROWS = 4
NUMBER = 65
SPACE = 4
for i in range(0, ROWS):
    for j in range(0, SPACE):
        print(end=" ")
    SPACE = SPACE-1
    for j in range(0, i + 1):
        print("",chr(NUMBER), end="")
        NUMBER += 1
    print("")
