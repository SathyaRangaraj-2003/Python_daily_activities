#activity_03

# soln1
n = int(input())

for i in range(0,n):
	for j in range(0,i+1):
		print("*",end =" ")
	print("\n")
	

# soln 2:

n = int(input())

for i in range(0,n+1):
	print("*" * i)

'''
*

* *

* * *

* * * *

* * * * *
'''