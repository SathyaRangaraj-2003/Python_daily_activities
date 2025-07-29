#activity_05:

#soln 1:
# 3 inputs
v1 = input("Enter the input1 :")
v2 = input("Enter the input2 :")
v3 = input("Enter the input3 :")

if (any(v1) and any(v2) and any(v3)) and  v1 != v2 != v3:
	print("All unique and non-empty")
	

#soln 02:
# 3 inputs
v1 = input("Enter the input1 :")
v2 = input("Enter the input2 :")
v3 = input("Enter the input3 :")

if (bool(v1) and bool(v2) and bool(v3)) and (v1 != v2 and v1 != v3 and v2 != v3):
	print("All unique and non-empty")
	

#soln 03:
# 3 inputs
v1 = input("Enter the input1 :")
v2 = input("Enter the input2 :")
v3 = input("Enter the input3 :")

if all([v1,v2,v3]) and (v1 != v2 and v1 != v3 and v2 != v3):
	print("All unique and non-empty")
