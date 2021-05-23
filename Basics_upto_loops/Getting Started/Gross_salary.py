'''program to calculate gross salary of ramesh'''

__author__ = "Shakir Sadiq"

Basic_Salary = float(input('Enter basic salary= ')) #basic salary
Dearness_allowance = 0.4 * Basic_Salary #dearnessallowance
Rent_allowance = 0.2 * Basic_Salary #Rentallowance
Gross_Salary = Basic_Salary + Dearness_allowance + Rent_allowance #Grosssalary
print('Dearness Allowance=' ,Dearness_allowance)
print('Rent Allowance=' , Rent_allowance)
print('Gross Salary=', Gross_Salary)
