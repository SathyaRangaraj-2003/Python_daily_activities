#activity_02:
#GCD

#soln 1:
n1 = int(input("Enter the integer 1: "))
n2 = int(input("Enter the integer 2: "))

gcd = 1
for i in range(1, min(n1,n2)+1):
	if n1 % i == 0 and n2 % i == 0:
		gcd = i
print(gcd)


#soln 2:

n1 = int(input("Enter the integer 1: "))
n2 = int(input("Enter the integer 2: "))

def gcd(a,b):
	if b :
		return gcd(b, a % b)
	else:
		return a

print(gcd(n1,n2))