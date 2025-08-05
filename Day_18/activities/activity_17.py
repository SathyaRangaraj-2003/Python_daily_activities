#activity_17:

num = int(input("Enter the number: "))
res = lambda x : x if x%2==0 else raise ValueError("Number is Odd")
print(res(num))