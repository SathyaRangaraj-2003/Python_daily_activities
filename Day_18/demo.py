# #lambda

# def func(a,b):
#     print( lambda a, b : a**2 + b**2 + 2*a*b)
# func(2,3)


# multiply = lambda x,y:x*y
# print(multiply (3,4) is 12)

# multiply = lambda x,y:x*y
# print(multiply(3,4))

# square = lambda x : x ** 2
# print(square(5))

N = int(input())
def square(n):
    s = lambda x:x**2
    return s(N)
print(square(N))

# f = lambda x : return  x*2
# print(f(3)) #error




# #built-in
# import math
# N = int(input())
# def square(n):
#     s = lambda x:math.sqrt(x)
#     return s(N)
# print(square(N))

# f = lambda : 42
# print(f()) # without arguments its working

# f = lambda x : (x+2,x*2)
# print(f(3)) =>#return tuple

# #print square root
# my_list = (1,2,3,4,5,6)
# result = list(map(lambda x : x**2,my_list))
# print(result)

# #if odd cube it else square
# my_list = (1,2,3,4,5,6)
# result = list(map(lambda x : x**3 if (x%2!=0) else x**2,my_list))
# print(result)

# #print even
# my_list = (1,2,3,4,5,6)
# result = list(filter(lambda x : x%2==0 ,my_list))
# print(result)

# # print prime
# import math
# def is_prime(x):
#     is_prime = 1
#     for i in range(2,int(math.sqrt(x))+1):
#         if x%i==0:
#             is_prime = 0
#     if is_prime :
#         return x

# my_list = (1,2,3,4,5,6)
# result = list(filter(lambda x : is_prime(x) ,my_list))
# print(result)


# #multiply
# from functools import reduce
# my_list = (1,2,3,4,5,6)
# result = reduce(lambda x,y : x*y ,my_list)
# print(result)

# #multiply without duplicate
# from functools import reduce
# my_list = (1,2,3,4,5,6,5)
# s = set(my_list)
# result = reduce(lambda x,y : x*y ,s)
# print(result)

# l=[1,2,3,4,5]
# squares = [x * x for x in l]
# print(squares)

# #odd
# l=[1,2,3,4,5]
# squares = [x * x for x in l if x%2!=0]
# print(squares)

# #prime
# #soln 1:
# import math
# def is_prime(x):
#     is_prime = 1
#     for i in range(2,int(math.sqrt(x))+1):
#         if x%i==0:
#             is_prime = 0
#     if is_prime :
#         return x

# l=[1,2,3,4,5]
# squares = [x * x for x in l if is_prime(x)]
# print(squares)

# #soln 2:
# #prime
# import math
# l=[1,2,3,4,5]
# prime =[]
# for i in l:
#     is_prime = 1
#     for j in range(2,int(math.sqrt(i))+1):
#         if i%j==0:
#             is_prime = 0
#     if is_prime :
#         prime.append(i)
# print(prime)
# print()

# squares = [x * x for x in l if x in prime]
# print(squares)

# #error look in this
# l=[1,2,3,4,5,6,7]
# res=[]
# labels = [res.append((x,"even")) if x%2==0 else res.append((x,"odd")) for x in l]
# print(labels)

# #nested list comprehension
# pair = [(x,y) for y in range(2) for x in range(3)]
# print(pair)


# #dictionary comprehension
# # if key is odd we need to square root
# s = {x : x**0.5 for x in range(10) if x%2!=0}
# print(s)

#list of tuples => this is dictionary reverse answer

# data = [("a",1),("b",2),("c",3),("b",4)]
# print({v:k for (k,v) in data})

# l=["one","Two","Three","four"]
# print({i:v for i,v in enumerate(l,start=1)})


# #x,y,z in range() single for
# c = {(x,y,z) : x*y*z for x in range(2) for y in range(2) for z in range(2)}
# print(c)

# s = (x*x for x in range(5))
# print(s)
# print(next(s))
# print(next(s))
# print(list(s))


# #walrus operator:
# try:
#     v1 = int(input("Enter the integer"))
# except ValueError:
#     v1 = int(input("Already given input is wrong Enter the correct integer"))

# try:
#     print("fsffd")
# except:
#     print("fdfv")
# else:
#     print("dvfd")


#  You have a list of students, each with a list of scores. Create a dictionary mapping the names of students who have an average score of 90 or higher to their average score.
# Concepts: nested list, list of dict, filter, map, lambda, dictionary comprehension.