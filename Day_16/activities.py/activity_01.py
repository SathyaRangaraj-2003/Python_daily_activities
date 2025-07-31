
#activity_01:
#linear search

#soln 1: for printing position
l_data = [10,20,30,60,40,100]
target = 40
for i in range(len(l_data)):
	if l_data[i] == target:
		print(i)
		break
else:
	print("-1")


#soln 2:
str = "sathya"
target = 'a'
for item in str:
	if item == target:
		print("Found")
		break
else:
	print("Not Found")