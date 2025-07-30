#activity_08:

#soln 1:
names = ["Alice" , "Bob" , "Charlie"]
marks = [85 , 90 , 88]
grades = ["B", "A", "A"]

for i,(name,mark,grade) in enumerate(zip(names,marks,grades)):
	print(i+1,name,mark,grade)



#soln2:
names = ["Alice" , "Bob" , "Charlie"]
marks = [85 , 90 , 88]
grades = ["B", "A", "A"]

for i in range(len(names)):
	print(i+1,names[i],marks[i],grades[i])