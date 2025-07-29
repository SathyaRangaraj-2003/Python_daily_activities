#activity_17:
#soln 01:
str = input("Enter the string : ")
l=list(str)
l.reverse()
if list(str) == l:
	print("Mirror")
else:
	print("Broken")

#soln 2:
str = input("Enter the string : ")
reversed_string = "".join(reversed(str))
if str == reversed_string:
	print("Mirror")
else:
	print("Broken")