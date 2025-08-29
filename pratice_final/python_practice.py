
# # 1. How do you reverse a string in Python without using slicing?
# #should not apply thi :

# s = "Sathya"
# print(s[::-1])

# #Reverse a string:

# #soln 1:
# s = "Sathya"
# res =""
# for char in s:
# 	res = char + res
# print(res)

# #soln 2:
# s = "Sathya"
# res =""
# for i in range(len(s)-1 , -1 , -1):
# 	res += s[i]
# print(res)


# #Write a program to check if a string is a palindrome.

# #soln 1:
# str = input("enter the string:")
# i=0
# j=len(str)-1
# while(i<j):
#     if(str[i] != str[j]):
#         print("Not a palindrome")
#         break
#     i+=1
#     j-=1
# else:  
#     print("Palindrome")

# #soln 2:
# s1 = input("enter the string:")

# if s1 == s1[::-1]:
#     print("palindrome")
# else:
#     print("Not alindrome")

# #soln 3:
# s1 = input("enter the string:")
# s2 = list(s1)

# if s2 == list(reversed(s2)):
#     print("palindrome")
# else:
#     print("Not palindrome")

# How do you remove duplicate characters from a string while maintaining order?
str = input("enter the input:")
str2 = set(str)
res=""
for chr in str:
    if chr in str2:
        res+=chr   
        str2.remove(chr)
print(res)