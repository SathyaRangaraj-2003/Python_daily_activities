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

'''Python Programming Challenge: Smart Input Validation
 
Problem Statement:
Write a single-line Python program that asks the user for a number. If the user enters a valid numeric string (digits only), use that value. If the user enters anything non-numeric (letters, symbols, etc.), prompt them again with a different message and use the second input.
 
Requirements:
Must be written in exactly one line of code
Cannot use if, else, elif statements
Cannot use and, or, not operators
Cannot use loops (for, while)
Cannot use functions or lambda expressions
Cannot use list comprehensions or dictionaries
Cannot use exception handling (try/except)
Should only prompt for the second input when the first input is invalid
 
Expected Behavior:
Test Case 1:
Enter the number: 123
(Program should use 123, no second prompt)
 
Test Case 2:  
Enter the number: abc
Kindly enter numeric value: 456
(Program should use 456)'''

# # soln 1: =>error
# num=int(input("Enter the number :"))
# print((num%3==0 * "jugs") or num)

# # soln2: =>if we give three instead of number or str
# num=input("Enter the number :")
# value=((num.isdigit() and int(num))  or int(input("enter numeric value :")))
# print((value%3==0 and "jugs") or value)


# #soln 3 =>error
# num = ((input("Enter the number: ").isdigit()) and int(input("Enter the number again: ")))  or int(input("Enter numeric value: "))
# print((num % 3 == 0 and "jugs") or num)

# #demo ==>error 
# ip = int(input("Enter the number: ").isdigit()  or input("Kindly enter numeric value: "))
# print(ip)

# # soln 4 => error => temporary can achieve(walrus operator)(:=) =>short circuit logic   =>(variable := expression)
# num = (input("Enter the number: ").isdigit())  or int(input("Enter numeric value: "))
# print((num % 3 == 0 and "jugs") or num)

# # ex:
# v1=5
# ip=(v1:=False) or 50
# print(ip)

# soln 5:=>final solution
#print(0 and 1 or 1)
# num = int((v1:=input("Enter the number: ")).isdigit() and v1 or input("Enter numeric value: "))
# print((num % 3 == 0 and "jugs") or num)

#jugs,mugs 
# num = int((v1 := input("Enter the number: ")).isdigit() and v1 or input("Enter numeric value: "))
# print((num % 3 == 0 and num % 5 == 0 and "jugs mugs") or (num % 3 == 0 and "jugs") or (num % 5 == 0 and "mugs") or num)


#jugs mugs pugs,jugs mugs,jugs mugs,mugs pugs,jugs(3),mugs(5),pugs(7) => 7 combination
# num = int((v1 := input("Enter the number: ")).isdigit() and v1 or input("Enter numeric value: "))
# print((num % 3 == 0 and num % 5 == 0 and num % 7 == 0 and "jugs mugs pugs") or (num % 3 == 0 and num % 5 == 0 and "jugs mugs") or (num % 3 == 0 and num % 7 == 0 and "jugs pugs") or (num % 5 == 0 and num % 7 == 0 and "mugs pugs") or (num % 3 == 0 and "jugs") or (num % 5 == 0 and "mugs") or (num % 7 == 0 and "pugs") or num)



# num=33

# num = int((v1:=input("Enter the number: ")).isdigit() and v1 or input("Enter numeric value: "))
# hund=num//10
# unit= num%10
# print((hund % 3 == 0 and "jugs")  or hund , (unit % 3 == 0 and "jugs")  or unit )


# num = int((v1:=input("Enter the number: ")).isdigit() and v1 or input("Enter numeric value: "))
# print(list(num))
# print((hund % 3 == 0 and "jugs")  or hund , (unit % 3 == 0 and "jugs")  or unit )



# str="sathy123 "
# print(str.isalnum())
# print(str.isalpha())







