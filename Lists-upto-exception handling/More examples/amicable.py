'''WAP to find the sum of all amicable numbers under 10000'''

__author__ = "Shakir Sadiq"

def amicable_sum(num):
    '''function for amicable numbers sum'''
    divisor_sum = [0] * num
    for i in range(1, len(divisor_sum)):
        for j in range(i * 2, len(divisor_sum), i):
            divisor_sum[j] += i
    result = 0
    for i in range(1, len(divisor_sum)):
        j = divisor_sum[i]
        if j != i and j < len(divisor_sum) and divisor_sum[j] == i:
            result += i
    return str(result)
print("\nThe sum of all amicable numbers under 10000: ",end="")
print(amicable_sum(10000))
