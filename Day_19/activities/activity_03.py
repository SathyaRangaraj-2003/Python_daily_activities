#activity_03:

from datetime import date
 
year, month, day = map(int, input("Enter your date of joining (YYYY-MM-DD): ").split('-'))
d = date(year, month, day)
today = date.today()
 
days_worked = (today - d).days
years_worked = days_worked // 365
months_worked = (days_worked % 365) // 30
 
print(f"Days completed: {days_worked}")
print(f"Years: {years_worked}, Months: {months_worked}")