'''Create a dictionary of anything. Print each element of
dictionary equal number of times to its place'''

car = {'brand':'ford','model':'mustang', 'year':'2013', 'colour':'black','number':'4312'}
for i in range(len(car)):
    element = (list(car.items())[i])
    print(i*(element,))
