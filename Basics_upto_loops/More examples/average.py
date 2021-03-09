'''Take 10 integers from keyboard and print their average'''

COUNT = 0
SUM = 0
for number in range(0,10):
	number = int(input("Enter number:"))
	SUM = SUM + number
	COUNT += 1
print("Average of the above numbers are: ", SUM/10)
