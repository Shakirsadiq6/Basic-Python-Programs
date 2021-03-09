'''update list’s elements at even places with increment of 1
and elements at odd places with increment of 2.'''

numbers = [23,12,37,86,63,52,98,47]
print("List of numbers before:", numbers)
for i in range(0,8,2):
    numbers[i] = numbers[i]+1
for i in range(1,9,2):
    numbers[i] = numbers[i]+2
print("\nList of numbers after:", numbers)
