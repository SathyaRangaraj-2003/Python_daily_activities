#activity_03:


import csv


with open('data.csv',newline='') as f:
	reader = csv.reader(f,quotechar = "-",quoting = csv.QUOTE_MINIMAL)
	data = list(reader)
	for row in data:
		print(row[1])
	





'''

data = [["name","age","city"], ["alice",35,"london"], ["bob",40,"newyork"]]
with open('data.csv','w',newline='') as f:
	writer = csv.writer(f)
	writer.writerows(data)
'''