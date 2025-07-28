

#print "pass" only if marks are at least the cutoff.
#without comparison operators



# #correct soln not absolute:
# #input
# marks ,cutoff= map(int,input("Enter the marks out of 100 : ").split(","))

# #process and result
# if(marks - cutoff ):
# 	print("Pass")

#corrected one
#input
marks = int(input("Enter the marks out of 100 : "))
cutoff = int(input("Enter the cutoff : "))
#process and result
diff = marks - cutoff
if(diff + abs(diff))//2 is diff:
	print("Pass")



# #soln 1:
# #input
# marks = int(input("Enter the marks out of 100 : "))
# cutoff = int(input("Enter the cutoff : "))
# #process and result
# if(marks//cutoff):
# 	print("Pass")

# # soln 2:
# #input
# marks ,cutoff= map(int,input("Enter the marks out of 100 : ").split(","))
# #process and result
# if(marks - cutoff or marks is cutoff):
# 	print("Pass")


# # Soln 3:
# #input
# marks = int(input("Enter the marks out of 100 : "))
# cutoff = int(input("Enter the cutoff : "))
# #process and result
# diff = marks - cutoff
# if(~diff ):
# 	print("Pass")


'''
#soln with condition operators:
#input
marks = int(input("Enter the marks out of 100 : "))
cutoff = int(input("Enter the cutoff : "))

#process and result
if(marks >= cutoff):
	print("Pass")

'''
