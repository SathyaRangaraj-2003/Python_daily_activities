#activity_16:

try:
	lst = [1,2,3,4,5,6]
	target = int(input("Enter the element to access..: "))
	print(lst[target] , "-> Found")
except IndexError:
	print("Out of bounds")
