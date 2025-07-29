#activity_12:
#input numbers,print "ascending" if sorted,"Descending" if in descending order,else "unordered"

num = input("enter the number :").split(",")
l = list(num)
if sorted(l) == num:
	print("Ascending")
elif sorted(l, reverse = True) == num:
	print ("Descending")
else:
	print ("Unordered")