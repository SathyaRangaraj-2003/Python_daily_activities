#activity_04:

employees = [("Alice" , 28 , 52345.75), ("Bob", 35 , 62300.5 ), ("Charlie" ,41, 70000.0) , ("Dana" ,25 ,48750.2),]


print("%-10s %3s %11s" % ("Name","Age","Salary"))

for name,age,salary in employees:
	print("%-10s %3d %011.2f" % (name,age,salary))
