#inputs
previous = int(input("Enter the previous reading : "))
current = int(input("Enter the current reading : "))

#units
units = abs(previous - current)

if units <=400:
	print("Bill Amount :" ,units * 4.80)
elif units >= 401 and units <= 500:
	print("Bill Amount :" ,units * 6.45)
elif units >= 501 and units <= 600:
	print("Bill Amount :" ,units * 8.55)
elif units >= 601 and units <= 800:
	print("Bill Amount :" ,units * 9.65)
elif units >= 801 and units <= 1000:
	print("Bill Amount :" ,units * 10.70)
else:
	print("Bill value :" ,units * 11.80)

