#activity_10:

data = {'a': 1, 'b': 2, 'c': 1}

dict = {}
for k,v in data.items():
	dict.setdefault(v,[]).append(k)

res = {k:tuple(v) for k,v in dict.items()}
print(res)