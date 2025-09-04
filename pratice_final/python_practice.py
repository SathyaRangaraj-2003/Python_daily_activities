
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


# #2. Write a program to check if a string is a palindrome.

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

# # 3.How do you remove duplicate characters from a string while maintaining order?
# # soln1:
# str = input("enter the input:")
# str2 = set(str)
# res=""
# for chr in str:
#     if chr in str2:
#         res+=chr   
#         str2.remove(chr)
# print(res)

# # soln2:
# str = input("enter the input:")
# res=""
# for chr in str:
#     if chr not in res:
#         res+=chr   
# print(res)

# # 4.Write a program to find the first non-repeating character in a string.
# # soln 1:
# str = input("Enter the input:")
# d = {}
# for chr in str:
#     if chr not in d:
#         d[chr] = 1
#     else:
#         num = d[chr]
#         d[chr] = num + 1
        
# # print(d)
# for val in d:
#     if d[val] == 1:
#         print(val)
#         break

# # soln 2:
# str = input("Enter the input:")
# for chr in str:
#     if str.count(chr):
#         print(chr)
#         break

# #5. How do you count the occurrence of each character in a string?
# str = input("Enter the input:")
# d = {}
# for chr in str:
#     if chr not in d:
#         d[chr] = 1
#     else:
#         d[chr] += 1
# print(d)



# #data structure:

# #  qn:01 Given two sets, find the symmetric difference without using .symmetric_difference().
# s1 = {1,2,3,4}
# s2 = {3,4,5,6}
# print(s1 ^ s2)

# #  qn:02 Check whether a list contains any duplicate elements using sets.
# # i/p : numbers = [3, 7, 2, 5, 3, 9] o/p : Contains duplicates: True

# numbers = [3, 7, 2, 5, 3, 9]
# set1 = set(numbers)
# # print(set1)
# if len(numbers) != len(set1):
#     print("Contains duplicates: True")
# else:
#     print("Contains duplicates: False")

# #qn: 03 Find all unique elements in a list of lists using set operations.
# # i/p : list_of_lists = [[1, 2], [2, 3], [4, 1]]
# # o/p : {1, 2, 3, 4}

# # soln 1:
# lst = [[1, 2], [2, 3], [4, 1]]
# res = set()
# for i in lst:
#     set1 = set(i)
#     res = res.union(set1)
# print(res)

# # soln 2: set operations
# lst = [[1, 2], [2, 3], [4, 1,2]]
# res = set()
# for i in lst:
#     res.update(i)
# print(res)

# #  qn :04 Count the frequency of words in a paragraph using a dictionary.
# #  i/p : paragraph = "Python is great and Python is easy to learn"
# #  o/p : {'Python': 2, 'is': 2, 'great': 1, 'and': 1, 'easy': 1, 'to': 1, 'learn': 1}

# paragraph = "Python is great, and Python is easy to learn!"
# cleaned = ''.join([chr for chr in paragraph if chr.isalnum() or chr.isspace()])
# data = cleaned.lower()

# lst = list(map(str,data.split(' ')))
# dit = {}
# for i in lst:
#     # dit[i] = dit.get(i, 0) + 1
#     if i in dit:
#         dit[i] += 1
#     else :
#         dit[i] = 1
# print(dit)


# # qn:05 Merge two dictionaries and sum values for common keys.
# # i/p : dict1 = {'a': 10, 'b': 20, 'c': 30} dict2 = {'b': 5, 'c': 15, 'd': 25}
# # o/p :{'a': 10, 'b': 25, 'c': 45, 'd': 25}

# dict1 = {'a': 10, 'b': 20, 'c': 30}
# dict2 = {'b': 5, 'c': 15, 'd': 25}
# for item in dict2:
#     if item in dict1:
#         dict1[item] += dict2[item]
#     else:
#         dict1[item] = dict2[item]
# print(dict1)


# # qn : 06 Given a dictionary of student scores, find the top three students.
# #  i/p :student_scores = {"Alice": 88,"Bob": 95,"Charlie": 91,"David": 85,"Eva": 92}
# #  o/p :
# # top_three = [
# #     ("Bob", 95),
# #     ("Eva", 92),
# #     ("Charlie", 91)]

# student_scores = {
#     "Alice": 88,
#     "Bob": 95,
#     "Charlie": 91,
#     "David": 85,
#     "Eva": 92

# }
# x = sorted(student_scores.items(),key=lambda item: item[1],reverse=True)[:3]
# print(x)


# # qn :09 Write a program to invert a dictionary so that keys become values and values become keys.
# # i/p : original_dict = {
# #     "Alice": 88,
# #     "Bob": 95,
# #     "Charlie": 91
# # }

# original_dict = {
#     "Alice": 88,
#     "Bob": 95,
#     "Charlie": 91
# }
# res = dict(zip(original_dict.values(),original_dict.keys()))
# print(res)


S='abcda'
k=2

def function(S,k):
    chunks = [S[i:i+k] for i in range(0, len(S), k)]
    chunks.sort(key=len)
    return ''.join(chunks)
print(function(S,k))