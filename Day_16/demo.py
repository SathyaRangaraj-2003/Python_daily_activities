# #without return 
# def greet(name):
#     print(f"hello ,{name}")

# #function with return 
# def mul(n):
#     return n * n

# str = input()
# n=int(input())
# greet(str)
# print(mul(n))

# #without return 
# def square(x):
# 	return x * x
# print(square(5)) #none


# #return type => int
# def square(x):
# 	return x * x
# print(type(square(5)))

# #multiple values
# #function return =>default tuple

# def sts(x,y):
#     return [x+y,x*y] #=>return list
# print(sts(2,5))
# print(type(sts(2,5)))


# def f(a,x=[]):
# 	x.append(a)
# 	return x
# print(f(1))
# print(f(2))


# #returning built-in function
# def s(x):
#     return sum(x)
# x=[1,2,3]
# print(s(x))


# #user-defined
# def s(x):
#     return d(x)
# def d(x):
#     return x * x
# x = 5
# print(s(x))

# #cannot assign value in return
# def t():
#     return x=5 #error
# print(t())

# #override
# def add(x,y):
#     return x+y
# def add(x,y):
#     return x*y
# print(add(3,4))


# #position arguments =<assign left to right
# def d(n,d):
#     return n/d
# print(d(2,10))

# #keyword arguments #no order
# def d(n,d):
#     return n/d
# print(d(d=2,n=10))

# must follow position
# def d(n,d):
#     return n/d
# print(d(n=10 ,5))  


#default parameters
# #time="morning" after default  parameter 
# # positional argument follows keyword argument
# def g( name,time="morning"):
#     print(time,name)

# print( g("Alice"))


# a=[1,2,3]
# b=[5,6]
# c=a
# print(id(a),a,id(b),b,id(c),c)

# #quiz
# def ex_list(val,lst=[]):
# 	lst+=[val]
# 	return lst
# v1=(ex_list(1))
# v2=ex_list(2,[])
# v3=(ex_list(3))
# v4=(ex_list(4))
# print(f"{id(v1)},{v1},{id(v2)},{v2},{id(v3)},{v3},{id(v4)},{v4}")

# #*args
# def tot(*args):
#     print(args)
#     return sum(args)
# print(tot(2,3,5,4))
# print(tot(2,3.4))
# print(tot(10))

# def foo(args):
#     print("args:",args) #error *args need to use
# foo(1,2,3)

# def show (**kwargs):
#     print(kwargs)
# show("name",age=30) #error


# def tag(*args,**kwargs):
#     print("[log]:",*args,**kwargs)

# tag("Hello","world",sep="~",end="@@")