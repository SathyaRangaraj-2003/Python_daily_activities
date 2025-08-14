

'''List: 2, 3, 4, 5, 6, 7, 8, 9, 10
p = 2: Mark multiples of 2 as composite: 4, 6, 8, 10. List becomes: 2, 3, (4), 5, (6), 7, (8), 9, (10).
p = 3: Next unmarked number is 3. Mark multiples of 3 as composite (starting from 3^2=9): 9. List becomes: 2, 3, (4), 5, (6), 7, (8), (9), (10).
p = 5: Next unmarked number is 5. Since 5^2 (25) is greater than 10, the process stops.
Result: The prime numbers less than or equal to 10 are 2, 3, 5, and 7'''










#by seive algorithm
'''
import math
n = int(input("Enter the input :"))


l1 = [1]
for i in range(2,n+1):
	is_prime=1
	for k in range(2,int(math.sqrt(n))+1):
		if n%k==0:
			is_prime = 0

	if is_prime and (i not in l1):
		l1.append(i)

	for j in range(i , n+1):
		if j % i != 0 and (j not in l1):
			l1.append(j)
	
	print(l1)

'''
'''
import math
n = int(input("Enter the input :"))


l=[]
for i in range(1,n+1):
	l.append(i)


while():
	#print(j)
	for k in range(2 , len(l)):
		if j != 1 and (l[k] != j) and (l[k] % j ==0):
			print(l.remove(l[k]))
	print(l)'''

'''
n = int(input("Enter the input :"))
iteration = n // 2
l=[]
for i in range(2,n+1):
      l.append(i)

i = 2
while(iteration and i<=n):
      for j in range(3 , n+1):
            if (j in l) and (i != j) and (j % i == 0):
                  l.remove(j)
      i+=1
      iteration -=1
      print(l)

'''
'''
n = int(input("Enter the input :"))
iteration = n // 2
l=list(range(2,n+1))
for i in range(2 , n+1):
	for j in range(3 , n+1):
		if (j in l) and (i != j) and (j % i == 0):
			l.remove(j)
	iteration -=1
	if iteration == 0:
		break
	print(l)

'''


'''
n = int(input("Enter the input :"))
iteration = n // 2
l=list(range(2,n+1))
for i in l:
	for j in l:
		if (j in l) and (i != j) and (j % i == 0):
			l.remove(j)
	iteration -=1
	if iteration == 0:
		break
	print(l)
'''


























