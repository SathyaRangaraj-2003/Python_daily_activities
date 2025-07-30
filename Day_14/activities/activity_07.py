#activity_07:
#input 2 integer ,if one is divisible by other print larger,else print sum.

a,b = map(int,input("Enter 2 numbers: ").split(","))
print("Larger" if a%b==0 or b%a==0 else a+b)



#correct soln
a,b = map(int,input("Enter 2 numbers: ").split(","))
if a!=0 and a%b==0:
    print(b)