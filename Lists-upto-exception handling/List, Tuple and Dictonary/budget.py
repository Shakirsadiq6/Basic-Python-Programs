'''Ask the customer his budget or range for expenditure
and return items from list which lies under his/her budget.'''

item = []
prices = []
for i in range(0, 5):
    elements = input("\nEnter item: ")
    price = int(input("Enter the price of item: "))
    item.append(elements)
    prices.append(price)
dict_items = dict(zip(prices,item))
budget = int(input("\nEnter budget="))
print("\nList of items which are under budget:",[dict_items[i] for i in dict_items if i <= budget])
