#expression by tuple operation(concatenation,replication,membership)

a=(1,2,3) #input1
b=(3,5,6) #input2

# 	       true  * (conactenation)*3 *  true 
print(a*2)
print((a not in b) , (a+b)*3   , (a[2] in b))    #single line of code