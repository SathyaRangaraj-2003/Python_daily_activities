
#quiz

# import math
# x = 10
# y = 25

# def add():
#     x = 3
#     y = 5
#     return x + y

# def mul():
# 	y = 2
# 	return x * y

# print(math.sqrt(5))
# # print(math.sqrt(x = 5)) #error
# print(add())
# print(mul())


# x ="Global"
# def outer():
#     def inner():
#         print(x)
#     x = "Enclosing"
#     return inner
# f=outer()
# f()


# # try : where to use yield and return


# #differ in return and yield
# # return terminates => regular funtion
# #  yield continues =>pause and resume
# # => generator function
# def odd(num):
#     n=0
#     while n<=num:
#         if n%2 ==1:
#             yield n
#         n +=1
# odd_num = odd(10)

# for i in odd_num:
#     print(i)

# print(next(odd_num))


# #docstring
# def greet():
#     '''sathya functions'''
#     return "sathya"

# print(greet.__doc__)