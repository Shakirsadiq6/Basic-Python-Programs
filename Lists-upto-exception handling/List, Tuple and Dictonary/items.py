'''User input names of 5 items. For each item, he/she input 3 different prices.
Now he/she ask customer’s budget and according to the budget return best offer
on items lying under his/her budget.'''

items = []
prices = []
offer = []
dict_items = {}
for elements in range(0, 5):
    element = input("Enter the name of item=")
    items.append(element)
    print("Enter 3 different prices of item:")
    prices.append([])
    for i in range(0, 3):
        price = int(input())
        prices[-1].append(price)
dict_items = dict(zip(items, prices))
print("\nThe items with different prices:",dict_items)
budget = int(input("\nEnter your budget="))
for i in range(0,5):
    print("\nBest offers on item",items[i],"under your budget:",[offer for offer in prices[i] if offer <= budget])
