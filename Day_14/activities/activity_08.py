#activity_08:
#sum first_two digits == sum last_two digits

num = input("Enter the 4-digit number : ")
if int(num[0]) + int(num[1]) == int(num[2]) + int(num[3]):
	print("Lucky")
else:
	print("Unlucky")
	
#need to check len should be 4