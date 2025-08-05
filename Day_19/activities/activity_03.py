#activity_03:

from datetime import date
date_of_joining = input("Enter date in format YYYY-MM-DD :")

d = date(date_of_joining)
print(d.year, d.month, d.day)