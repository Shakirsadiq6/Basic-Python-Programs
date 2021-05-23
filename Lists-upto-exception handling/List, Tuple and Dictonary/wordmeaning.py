'''Create a dictionary of words having their meaning. Return the difference between actual length
of dictionary and length of each element of dictionary. Pick the maximum value from several values
comes after difference and return word from dictionary at place equals to maximum value.'''

__author__ = "Shakir Sadiq"

words = {
'exist':'to be real',
'foul':'to make dirty',
'delete':'remove',
'element':'an essential',
'enervate':'morally drained'
}
minus = []
print("Actual length of dictionary:",len(words),"\n")
for i in range(len(words)):
    print("length of element at index",i,":",len(list(words.values())[i])+len(list(words.keys())[i]))
    print("difference between actual length and length of element at index",i,":",(len(list(words.values())[i])+len(list(words.keys())[i])-len(words)),"\n")
    minus.append(len(list(words.values())[i])+len(list(words.keys())[i])-len(words))
print("\nmaximum value from difference:",max(minus))
if max(minus)>len(words):
    print("maximum value is greater than the elements of the dictionary.")
else:
    print("word from dictionary at place to maximum value.",list(words.keys())[max(minus)])
