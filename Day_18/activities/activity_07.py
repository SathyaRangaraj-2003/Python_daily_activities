# i=i creates a new default value for each lambda

#activity_07:

funcs = [lambda i=i: i * 3 for i in range(1,4) ]
print([f() for f in funcs])