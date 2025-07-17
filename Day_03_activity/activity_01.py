# qn:01 a=5,b=10 find which is bigger

# soln 1:
a=5
b=10
x=(a + b + abs(a - b)) // 2
# x=f"{x} is bigger"
print(x)

# soln 2:
a=5
b=10
print(max(a,b))

# soln 3:
a=5
b=10
print((a + b - ((a - b) * (a - b)) // (a - b) ) // 2)

# soln 4:
a=5
b=10
print("v1 is greater than v2 - the statement is",a>b)
# o/p: v1 is greater than v2 - the statement is False
