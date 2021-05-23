'''WAP to find number of vowels, consonants, digits and white_spaces in a string'''

__author__ = "Shakir Sadiq"

DIGIT = 0
VOWELS = 0
CONSONANTS = 0
WHITE = 0
str= input("Enter a string=")
for i in range(0,len(str)):
    ch = str[i]
    if((ch>='a' and ch<='z')) or ((ch>='A' and ch<='Z')):
        ch=ch.lower()
    if (ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u'):
        VOWELS += 1
    if(ch>='0' and ch<='9'):
        DIGIT += 1
    if(ch == " "):
        WHITE += 1
    if(ch == 'b' or ch == 'c' or ch == 'd' or ch == 'f' or ch == 'g' or ch == 'h' or ch == 'j' or ch == 'k' or ch == 'l' or ch == 'm' or ch == 'n' or ch == 'p' or ch == 'q' or ch == 'r' or ch == 's' or ch == 't' or ch == 'v' or ch == 'w' or ch == 'x' or ch == 'y' or ch == 'z'):
        CONSONANTS += 1
print("Vowels=", VOWELS)
print("Consonants=", CONSONANTS)
print("Digits=", DIGIT)
print("Spaces=", WHITE)
