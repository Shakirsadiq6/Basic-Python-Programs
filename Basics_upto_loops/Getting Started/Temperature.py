'''convert Fahrenheit degrees temperature into Centigrade degrees'''

__author__ = "Shakir Sadiq"

Fahrenheit = float(input('Enter the temperature of city (in fahrenheit)= '))
Centigrade = (Fahrenheit-32)*(5/9)
print('The temperature in Centigrade degrees= ',Centigrade)
