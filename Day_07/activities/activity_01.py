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

# (walrus operator)(:=) =>short circuit logic   =>(variable := expression)

num = int((v1:=input("Enter the number: ")).isdigit() and v1 or input("Enter numeric value: "))
print((num % 3 == 0 and "jugs") or num)