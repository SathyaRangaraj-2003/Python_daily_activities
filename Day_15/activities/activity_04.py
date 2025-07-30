#activity_04

#soln1:
n = int(input())

for i in range(0,n):
	for j in range(i+1,n):
		print(" ",end="")
	for k in range(0,i+1):
		print("*",end="")
	for m in range(1,i+1):
		print("*",end="")
	print("\n")
	
#soln 2:
n = int(input())

for i in range(0,n+1):
	spaces = ' ' * (n-i)
	stars = '*' * (2 * i -1)
	print(spaces + stars)

'''
    *

   ***

  *****

 *******

*********
'''