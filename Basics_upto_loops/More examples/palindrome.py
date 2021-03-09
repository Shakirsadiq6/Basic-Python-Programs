'''Print palindrome numbers upto 1 million'''

MAXIMUM = 1000000
print("Palindrome Numbers upto 1 million")
for num in range(1, MAXIMUM + 1):
    temp = num
    reverse = 0   
    while(temp > 0):
        reminder = temp % 10
        reverse = (reverse * 10) + reminder
        temp = temp //10
    if(num == reverse):
        print(num, end ="")
        print()
		