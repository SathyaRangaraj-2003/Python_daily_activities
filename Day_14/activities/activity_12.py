#activity_12:
#input numbers,print "ascending" if sorted,"Descending" if in descending order,else "unordered"


num = input("Enter the numbers :").split(",")
if sorted(num) == num:
	print("Ascending")
elif sorted(num, reverse = True) == num: #num == sorted(num)[::-1]:  
	print ("Descending")
else:
	print ("Unordered")


# #soln 2:
# num = input("enter the number :").split(",")
# l = list(num)
# if sorted(l) == num:
# 	print("Ascending")
# elif sorted(l, reverse = True) == num:
# 	print ("Descending")
# else:
# 	print ("Unordered")