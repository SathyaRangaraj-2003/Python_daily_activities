#activity_05

#soln 1
num = int(input("enter the integer :"))
count=0
while (num >= 0):
	count += 1
	num -= 3
print("Loop ran for:",count)



#possible in for loop
#soln2
num = int(input("enter the integer :"))
count = 0
for i in range(num + 1):
	if(num < 0):
		break
	count+=1
	num -=3
print("Loop ran for:",count)