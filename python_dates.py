from datetime import date, timedelta

from functions_2 import volume_cylinder

today = date.today()
print(today.weekday())

f_date = today.strftime("%d-%m-%Y")
print(f_date)

f_date = today.strftime("%d-%m-%y")
print(f_date)

expiry_date = today -timedelta(days=365)
print(expiry_date)

date1 = date(2018, 12,13 )
date2 = date(2015, 2,25 )
difference = date1 - date2
print(difference)