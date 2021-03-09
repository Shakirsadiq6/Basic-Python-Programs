'''The largest palindrome made from the product of two 3 digit numbers'''

try:
    def palindrome(n):
        '''function to find product of two 3 digit numbers'''
        upper = (10**(n))-1
        lower = 1 + upper//10
        max_product = 0
        for i in range(upper,lower-1, -1):
            for j in range(i,lower-1,-1):
                product = i * j
                if product < max_product:
                    break
                number = product
                reverse = 0
                while number != 0:
                    reverse = reverse * 10 + number % 10
                    number =number // 10
                if (product == reverse and product > max_product):
                    max_product = product
        return max_product
    n = 3
    print("\nThe largest palindrome made from the product of two 3 digit numbers: ",end="")
    print(palindrome(n))
except ValueError:
    print("It is an invalid number!")
