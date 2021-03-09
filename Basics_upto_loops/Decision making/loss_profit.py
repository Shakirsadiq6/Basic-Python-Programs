'''program to determine whether the seller has made profit or incurred loss'''

cost_price = float(input('Enter the cost price= ')) #costprice
selling_price = float(input('Enter the selling price= ')) #sellingprice
profit = selling_price - cost_price
loss = cost_price - selling_price
if selling_price>cost_price:
    print('The seller made the profit of',profit)
elif cost_price>selling_price:
    print('The seller incurred the loss of',loss)
else:
    print('Seller made profit or incurred loss of 0')
	