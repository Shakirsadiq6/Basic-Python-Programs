'''Add first seven terms of 1/1! + 2/2! + 3/3! + ...'''

SUM = 0
for i in range(1,8):
    FACTORIAL = 1
    for j in range(1,i+1):
        FACTORIAL *= j
    division = i/FACTORIAL
    SUM += division
print("Sum of First Seven Terms=", SUM)
