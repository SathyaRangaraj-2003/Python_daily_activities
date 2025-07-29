#activity_15:

num1 , num2 = map(int,input("Enter two integers : ").split(","))

if (num1 % 2 != 0 or num2 % 2 != 0) and (num1 % 2 == 0 or num2 % 2 == 0):
	print("Exactly one is odd!")