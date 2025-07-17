# Print Only the Middle Digit of a 3-digit Number Scenario: Given a 3-digit number x = 426, print only the middle digit. 

#soln 01
# x=426
# y=str(x)
# print(y[1])

# #soln 02
# print((x // 10) % 10)

# #soln 03
# x=426
# y=str(x)
# print(y[1:2])


# #print() activity
# print("sum is:",2+3)
# print("greater is:",2>3)
# print("greater is:",int(2>3))
# #newline(\n)
# print("Hello, \nWorld")

# #custom separators:(sep) 
# print("2025","07","16",sep="-")

# # custom ending:(end)
# print("sathya",end="...")
# print("rangaraj")

# #split()
# x,y=input("enter 2 num: ").split(' ')
# print(x,y)

# #int,float
# #soln 1
# v1,v2=5,5.0
# print(f"int v1:{v1} \nfloat v2:{v2}")
# #soln 2
# v1,v2=input("enter int num:"),input("enter float num")
# print(f"int v1:{v1} \nfloat v2:{v2}")
# #soln 3
# v1,v2=input("enter 2 num: ").split(',')
# print(f"int v1:{v1} \nfloat v2:{v2}")

# #comma()
# x,y,z=input("enter 3 num: ").split(',')
# print(f'x:{x}\ny:{y}\nz:{z}')

# # type casting to integer using map:
# v1,v2,v3,v4,v5 = map(int,input("enter five nums: ").split(','))
# print(f'v1:{v1}\nv2:{v2}\nv3:{v3}\nv4:{v4}\nv5:{v5}')


# # f-String:
# name="sathya"
# marks=90
# print(f"name:{name} \nmarks:{marks}")

# #ascii
# print(ord('A')) 
# print(chr(97)) 

# #list
# mixed_sathya=[10,False,20,"sathya",40.0,None]

# #list()
# letters=list("hello")
# result=""
# result+=letters[0].upper()
# result+=letters[1].upper()
# result+=letters[2].upper()
# result+=letters[3].upper()
# result+=letters[4].upper()
# print(result)

# print(*list('hello'.upper()))

# a=[1,2,3,4]
# print(a)
# print(*a)

# print(*list('hello'.upper()))

# a=list("hello")
# for char in a:
#     print(chr(ord(char)-32),end="")
    
# # #join()  list
# #try 01
# words=["Geeks","For","Geeks"]
# str=""
# for val in words:
#     for char in val.lower():
#         str+=chr(ord(char)-32)
#     str+=" "
# print(str)
# print("".join(str))

# # try 02
# words=["Geeks","For","Geeks"]
# word=[]
# for val in words:
#     str=""
#     for char in val.lower():
#         str+=chr(ord(char)-32)
#     word.append(str)
# print(" ".join(word))

# words=["geeks","for","geeks"]
# num=[123,287,9001]
# print(str(num[2])[2])

# # try : 3rd 9001 change 3rd index 0=>3
# num=[123,287,9001]
# print(str(num[2])[2])


# #concatenation
# a=[1,2,3]
# b=[5,6]
# c=a+b
# print(c)
# print(type(c))

# # repetition(*)
# a=["hi","hello"]*3
# print(a)

# #membership operators (in,not in)
# a=["hi","hello"]
# print("yellow" in a)


# # methods

# #append()
# a=[1,2,3]
# a.append(30)
# print(a)

# #shallow copy
# a=[1,2,3]
# b=a
# b[0]=100
# print(a)
# print(b)

a=[1,2,3]
b=a.copy()
b[0]=100
print(a)
print(b)

# #count()
# a=[1,2,1,3,3,4,5,2,1]
# print(a.count(1))

# #entend() => to add one list
# a=[1,2,3]
# b=[4,5]
# c=[7,8,9]
# a.extend(c)
# print(a)

# #index()
# name=["alice","bob"]
# print(name[0].index('i'))
# print(name[name.index("alice")].index('i'))

# #remove
# a=[1,2,1,3,3,4,5,2,1]
# a.remove(1)
# print(a)

# #(1)try work (extend)
# #to add multiple list
# a=[1,2,3]
# b=[4,5]
# c=[7,8,9]
# print(*a,*b,*c)
# unpack=[*a,*b,*c]
# print(unpack)
# print(a+b+c)
# a.extend(b+c)  # by modifying the list
# print(a)

# #(2)try work: (index) =>first occurnce index
# num=[123,287,9001]
# print(str(num[2]).index('0'))
# print(num)

# #(3)try work =>remove all occurance
# a=[1,2,1,3,3,4,5,2,1]
# while 1 in a:
#     a.remove(1)
# print(a)

# a=[1,2,1,3,3,4,5,2,1]
# while a.count(1) > 0:
#     a.remove(1)
# print(a)


