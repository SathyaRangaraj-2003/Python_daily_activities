#activity_15:

def division():
	n = int(input("Enter numerator: "))
	while True:
		try:
			d = int(input("Enter denominator: "))
			print("Result:",n / d)
			break
		except ZeroDivisionError:
			print("Cannot divide by zero!")

division()