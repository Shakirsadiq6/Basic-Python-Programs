'''Create a list of Tuples of food items & make a dictionary of each item
with its category. No item should repeat itself if it exists in more
than one tuple. Make list of each category defined by dictionary.'''

__author__ = "Shakir Sadiq"

food_items = [('apple','orange','lays','mango'),('peas','apple','potato'),('pizza','burger','lays')]
print("\nList of food items:\n",food_items,"\n")
category = {
'fruits':['apple','orange','mango'],
'vegetables':['peas','potato'],
'junk':['pizza','burger','lays']
}
category_list = []
for key, value in category.items():
    category_list.append(key)
    category_list.append(value)
print("Category of food items:\n",category_list)
