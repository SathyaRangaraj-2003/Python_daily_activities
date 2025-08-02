#activity_05:

#first prime greater than n
import math
num = int(input("Enter the number :"))

def is_prime(num):
	if num <= 1:
		return False
	for i in range(2,int(math.sqrt(num))+1):
		if num % i == 0:
			return False
	return True

for n in range(num+1, 1001):
	if is_prime(n):
		print(n)
		break
else:
	print("Not found")