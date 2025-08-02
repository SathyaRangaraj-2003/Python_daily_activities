#activity_03:
#LCM

#soln 1:

n1 = int(input("Enter the integer 1: "))
n2 = int(input("Enter the integer 2: "))

def gcd(a,b):
	if b :
		return gcd(b, a % b)
	else:
		return a

LCM = (n1 * n2) / gcd(n1 , n2)
print(LCM)