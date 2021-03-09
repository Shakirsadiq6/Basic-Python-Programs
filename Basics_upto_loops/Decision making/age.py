'''determine the youngest of Ram, Shyam and Ajay'''

ram = int(input('Enter the age of Ram='))
shyam = int(input('Enter the age of Shyam='))
ajay = int(input('Enter the age of Ajay='))
if (ram<=shyam and ram<=ajay):
    print('The youngest is Ram, age=',ram)
elif (shyam<=ajay and shyam<=ram):
    print('The youngest is Shyam, age=',shyam)
else:
    print('The youngest is Ajay, age=',ajay)
