

#print "pass" only if marks are at least the cutoff.
#without comparison operators


'''
#correct soln:
#input
marks ,cutoff= map(int,input("Enter the marks out of 100 : ").split(","))

#process and result
if(marks - cutoff ):
	print("Pass")
'''

'''

#soln 1:
#input
marks = int(input("Enter the marks out of 100 : "))
cutoff = int(input("Enter the cutoff : "))


#process and result
if(marks//cutoff):
	print("Pass")



Soln 2:
#input
marks = int(input("Enter the marks out of 100 : "))
cutoff = int(input("Enter the cutoff : "))

#process and result
diff = marks - cutoff
if(~diff ):
	print("Pass")

'''


#input
marks ,cutoff= map(int,input("Enter the marks out of 100 : ").split(","))

#process and result
if(marks - cutoff or marks is cutoff):
	print("Pass")




'''
#soln:
#input
marks = int(input("Enter the marks out of 100 : "))
cutoff = int(input("Enter the cutoff : "))

#process and result
if(marks >= cutoff):
	print("Pass")

'''
