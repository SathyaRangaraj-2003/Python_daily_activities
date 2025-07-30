# #validation:

# #string
# str=''
# if str:
#     print("true")
# else:
#     print("false")

# #bool
# b=True
# if b:
#     print("true")
# else:
#     print("false")

# #nonetype
# a=None
# if a:
#     print("true")
# else:
#     print("false")

# #set
# s=set((1,2))
# # print(s)
# if s:
#     print("true")
# else:
#     print("false")

# #logical operators
# a=20
# if a>=18 and input():
#     print("elligible")

# r=True or False and False
# print(r) #true precedence


# a=17
# has_id=True
# is_member = True

# if a >=18 and has_id or is_member:
#     print("allowed")
# else:
#     print("not")

# #ternary operator
# print("sathya") if True else "rangaraj"

# #quiz
# d=[]
# print(all(d),any(d))  #true , false


# # operations bitwise:
# a=5
# print(~a)  # -(a+1) # -6

# s="sathya"
# v="Sathya"

# print(s==v)


'''
#activity_07:
#input 2 integer ,if one is divisible by other print larger,else print sum.

a,b = map(int,input("Enter 2 numbers: ").split(","))
print("Larger" if a%b==0 or b%a==0 else a+b)

'''

'''
#activity_08:
#sum first_two digits == sum last_two digits

num = input("Enter the 4-digit number : ")
if int(num[0]) + int(num[1]) == int(num[2]) + int(num[3]):
	print("Lucky")
else:
	print("Unlucky")
'''

'''
#activity_09:
#odd or even 
#without arithmetic operator

num = int(input("Enter the user-input integer : "))
if num & 1:
	print("Odd")
else:
	print("Even")
'''

'''
#activity_10:

#2-string ,print "match" if they are equal (case insensitive) else "no match"
#one if-statement(no ternary)

str1 = input("Enter the String 1 : ")
str2 = input("Enter the String 2 : ")

if str1.upper() == str2.upper():
	print("Match")
else:
	print("No match")
'''

''' 
#activity_11:
#one-liner ,only logical operators,no if,print "magic" for specific value ex: 42 else nothing

print(int(input("Enter the input num : ")) == 42 and "magic")
'''

'''
#activity_12:
#input numbers,print "ascending" if sorted,"Descending" if in descending order,else "unordered"

num = input("Enter the numbers :").split(",")
if sorted(num) == num:
	print("Ascending")
elif sorted(num, reverse = True) == num: #num == sorted(num)[::-1]:  
	print ("Descending")
else:
	print ("Unordered")
'''

'''
#activity_13:

num =  int(input("Enter the number :"))

if 10 < num < 20:
	print("Within Range")
'''

'''
#activity_14:

value = input("Enter the input: ")

if value == "0" or value == "False":
	print("Falsy")
else:
	print("Truthy")
'''

'''
#activity_15:

num1 , num2 = map(int,input("Enter two integers : ").split(","))

if (num1 % 2 != 0 or num2 % 2 != 0) and (num1 % 2 == 0 or num2 % 2 == 0):
	print("Exactly one is odd!")
'''
'''
#activity_16:

val1 , val2 ,val3=input("Enter 3 booleans : ").split(",")
print("Exactly one" if [val1,val2,val3].count("True") == 1 else "Nope")

'''
'''
#activity_17:
#soln 01:
str = input("Enter the string : ")
l=list(str)
l.reverse()
if list(str) == l:
	print("Mirror")
else:
	print("Broken")

#soln 2:
str = input("Enter the string : ")
reversed_string = "".join(reversed(str))
if str == reversed_string:
	print("Mirror")
else:
	print("Broken")

'''

