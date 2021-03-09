'''Print armstrong numbers in range of 1 million'''

LOWER = 1
UPPER = 1000000

for num in range(LOWER, UPPER + 1):
    order = len(str(num))
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10
    if num == sum:
        print(num)
