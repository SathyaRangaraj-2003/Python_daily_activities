#activity_02:

'''
import csv
with open("data.csv",newline='') as file:
	reader = csv.DictReader(file)
	sum = 0 
	for row in reader:
		sum += float(row["amount"])
print(sum)'''


import csv
with open("data.csv",newline='') as file:
	reader = csv.reader(file)
	next(reader)
	sum = 0 
	for row in reader:
		sum += float(row[1])
print(sum)