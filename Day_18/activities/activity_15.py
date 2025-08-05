#activity_15:


try:
	n = int(input("Enter numerator: "))
	d = int(input("Enter denominator: "))
	print("Result:",n / d)
except ZeroDivisionError:
	d = int(input("Cannot divide by zero! \nEnter denominator: "))
	if d != 0:
		print("Result: ",n / d)