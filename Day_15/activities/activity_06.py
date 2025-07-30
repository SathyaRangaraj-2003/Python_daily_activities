#activity_06

# soln1:
l1 = ["3456","s45a","00x0","00","--","0000"]

for l in l1:
	if l.count('0') == len(l):
		break
	elif l.isdigit():
		print(l)
	else:
		continue
	

# soln2
while True:
	code = input("Enter the code :")
	if code.count('0') == len(code):
		break
	elif code.isdigit():
		print(code)
	else:
		continue

	