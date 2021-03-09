''' Take input from user until he/she presses q. Print average and sum of all numbers'''

print("Start entering numbers=")
SUM=0
TOTAL=0
while 1:
    num=int(input())
    TOTAL=TOTAL+1
    SUM=SUM+num
    print("Press 'q' when you are done inputting the numbers or 'y' to continue")
    m=input()
    if m=='q':
        break    
print("Average=",SUM/TOTAL)
print("Sum=",SUM)
