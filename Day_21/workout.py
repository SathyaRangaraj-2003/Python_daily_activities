'''
# CSV reading => csv.reader()
#newline='' => to avoid blank lines

import csv
with open("data.csv",newline='') as f:
	reader = csv.reader(f)
	for row in reader:
		print(row)

#accessed by index
import csv
with open("data.csv",newline='') as f:
	reader = csv.reader(f)
	print(row[0])


# CSV reading without header
import csv
with open("data.csv",newline='') as f:
	reader = csv.reader(f)
	next(reader)
	for row in reader:
		print(row)

#csv data into all rows in single list,each row becomes sublist 
import csv
with open("data.csv",newline='') as f:
	reader = csv.reader(f)
	data = list(reader)
	print(data)

# .line_num
import csv
with open("data.csv",newline='') as f:
	reader = csv.reader(f)
	for row in reader:
		print(reader.line_num, row)


#CSV reading as dictionaries => csv.DictReader()
import csv
with open("data.csv",newline='') as f:
	reader = csv.DictReader(f)
	for row in reader:
		print(row["name"],row["age"])


#fieldnames in dictionary (column name will be displayed)
import csv
with open("data.csv",newline='') as f:
	reader = csv.DictReader(f)
	print(reader.fieldnames)

# .line_num => to display line number default from 2
import csv
with open("data.csv",newline='') as f:
	reader = csv.DictReader(f)
	for row in reader:
		print(reader.line_num) 


# CSV writing files => csv.writer()
#single row => writerow()
import csv
with open("output.csv",'w',newline='') as f:
	writer = csv.writer(f)
	writer.writerow(['name','age','city'])
	writer.writerow(['alice',30,'new york'])

#multiple rows => writerows()
import csv
rows = [["name","age","city"], ["alice",35,"london"], ["bob",40,"newyork"]]
with open('output.csv','w',newline='') as f:
	writer = csv.writer(f)
	writer.writerows(rows) 


#CSV writing as dictionary =>csv.DictWriter(file,fieldname=[])

import csv

data=[{'name': 'alice', 'age': '35', 'city': 'london'},
{'name': 'bob', 'age': '40', 'city': 'newyork'}]

with open('output.csv','w',newline='') as f:
	writer = csv.DictWriter(f , fieldnames = ['name','age','city'])
	writer.writeheader()     #to display with header
	writer.writerow({'name': 'charlie', 'age': '25', 'city': 'brazil'})
	writer.writerows(data)


#csv file reading with custom delimeter
import csv
with open("data.csv",newline='') as f:
	reader = csv.reader(f , delimiter = ';')
	for row in reader:
		print(row)


#csv file writing with custom delimiter

import csv
data=[["name","age","city"], ["alice",35,"london"], ["bob",40,"newyork"]]
with open("data.csv",mode='w',newline='') as f:
	writer = csv.writer(f , delimiter = ';')
	writer.writerows(data)

#Custom Quote character
#QUOTE_MINIMAL, QUOTE_ALL, QUOTE_NONNUMERIC , use escapechar for QUOTE_NONE
import csv
data = [["name","age","city"], ["alice",35,"london"], ["bob",40,"newyork"]]
with open('output.csv','w',newline='') as f:
	writer = csv.writer(f , quotechar = "$" , quoting = csv.QUOTE_NONNUMERIC)
	writer.writerows(data)



#escapechar
import csv
data = [["name","age","city"], ["alice",35,"london"], ["bob",40,"newyork"]]
with open('output.csv','w',newline='') as f:
	writer = csv.writer(f , quotechar = "$" , escapechar = '\\')
	writer.writerows(data)

'''




















