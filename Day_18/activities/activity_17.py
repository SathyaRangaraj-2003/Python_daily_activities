#activity_17:

try:
	num = int(input("Enter the number: "))
	res = lambda x : x if x%2==0 else x.throw(ValueError)
	print("Even Number:",res(num))
except:
	print("Odd Number")