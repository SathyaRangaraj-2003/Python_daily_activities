#activity_06:

lst = [(a,b,c)  for a in range(1,31) 
		for b in range(1,31) 
		for c in range(1,31) if a**2 + b**2 == c**2]
print(lst)

lst = [(a,b,c)  for a,b,c in zip(range(1,31),range(1,31),range(1,31)) if a**2 + b**2 == c**2]
print(lst)