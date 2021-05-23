'''Create a Tuple of eateries of name done by user.
Make an another tuple Surnames through user input and
then make third tuple by tagging each name with surname.'''

__author__ = "Shakir Sadiq"

list_tuple = []
single_list = []
eateries = tuple(input("Enter eateries: ").split())
surnames = tuple(input("Enter surnames: ").split())
print()
if len(eateries)>len(surnames):
    print("surname should have more elements than eateries")
else:
    for i in range(len(eateries)):
        list_tuple.append((eateries[i]+surnames[i]).split())
#convert multiple lists in single list
    single_list = [item for single_list in list_tuple for item in single_list]
    print("Third tuple by tagging each eateries name with surname =")
    print(tuple(single_list))
