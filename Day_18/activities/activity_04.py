#activity_04:

data = [('Alice', 90), ('Bob',75), ('Charlie', 90), ('Dave', 60)]

result = sorted(data,key = lambda x : (-x[1], x[0]))

print(result)