# # modifying tuple by list
# t=(
#     1,2,3,[8,10]
# )
# t[3][0]=45
# print(t)

# #or operator
# print(4 or 5)
# print(0 or 5)

'''
step 01: get input from user
step 02:if the number is divisible by 3 then print "jugs"
else print same number 
without if condition'''

# # soln 1:
# num=int(input("Enter the number :"))
# print((num%3==0 * "jugs") or num)

# soln2: =>if we give three instead of number or str
# num=input("Enter the number :")
# value=((num.isdigit() and int(num))  or int(input("enter numeric value :")))
# print((value%3==0 and "jugs") or value)


#soln 3
num = (input("Enter the number: ").isdigit() )  or int(input("Enter numeric value: "))
print((num % 3 == 0 and "jugs") or num)



