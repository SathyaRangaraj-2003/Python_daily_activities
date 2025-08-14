'''
read the input from 
if it is string,u should check the string is palindrome or  not,
if it is a number ,u need to print the given number is odd or even 
if the number is float ,length of digits.
if not all ,"not a valid type"

rules:
no type casting at beginning.
dont use condition.

case : 99
case : r.ram
case : 35e3

    7e-2   // Represents 7 * 10^-2 = 0.07
    5E-4   // Represents 5 * 10^-4 = 0.0005
'''

practice 1:

#user input
str=input("Enter the input String :")

#process

r1 = str.isdigit() and (int(str)%2==0 and ("Odd") or ("Even"))

r2 = str.count('.')==1 and len(str)-1

r3 = str.isalpha() and  (str == str[::-1] and ("String is palindrome") or ("String is not palindrome") ) 

#output
result =( r1 or r2 or r3 or "Not a Valid Type")
print(result)



practice 2:

#user input
str=input("Enter the input String :")

#process

r1 = str.isdigit() and (int(str)%2==0 and ("Odd") or ("Even"))

r2 = '.' in str 

r3 = str.isalpha() and  (str == str[::-1] and ("String is palindrome") or ("String is not palindrome") ) 

#output
result =( r1 or r2 or r3 or "Not a Valid Type")
print(result)



#r4 = str.count('.')>=1 and str.replace('.','') and str == str[::-1] and ("String is palindrome") or ("String is not palindrome")











