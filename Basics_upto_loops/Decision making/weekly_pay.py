'''program to calculate Weekly pay of a person'''

work_hours = int(input('Enter total work hours='))
hourly_wage = int(input('Enter regular hourly wage='))
total_pay = work_hours*hourly_wage #totalpay
extra_hours = work_hours-40 #extrahours
if work_hours<=40:
    print('Total pay=',total_pay)
elif 61>work_hours>40:
    extra_pay = (hourly_wage*40)+(1.5*hourly_wage*extra_hours) #extrapay >40
    print('Total pay=',extra_pay)
elif work_hours>60:
    extra_pays =(hourly_wage*40)+(2*hourly_wage*extra_hours) #extrapay >60
    print('Total pay=',extra_pays)
	