import csv

with open("data1.csv",newline="") as f:
	reader = csv.reader(f)
	for row in reader:
		if row:
			print(row)