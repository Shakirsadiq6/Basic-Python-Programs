''' Shop will give 10% discount if the cost of purchased quantity is more than 1000. print total cost.'''

__author__ = "Shakir Sadiq"

quantity = int(input("Enter quantity="))
one_unit_cost = 100
total_cost = one_unit_cost*quantity
total_cost_discount = 0.9*total_cost
if total_cost>1000:
    print("The total cost will be=",total_cost_discount)
else:
    print("The total cost will be=",total_cost)
