#activity_06:

#two space integer:
a,b = map(int,input("Enter the integer with spaces :").split(" "))

#swap
a=a^b
b=a^b
a=a^b

#print
print(a,b)