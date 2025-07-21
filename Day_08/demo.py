# #simple activity

# #list inside tuple gets modified
# t=(1,2,'python',[1000,(1,2)])
# t[3][0]=1
# print(t)
 
# #empty tuple cannot modified
# t=(1,2,'python',[1000,tuple()])
# print(t)
 
# #empty tuple not modified 
# t=(1,2,1000,tuple(map(int,input("number:"))))
# print(t)

# #with multiple inputs empty tuple not modified 
# t=(
#     2,3,[3,4,tuple(map(int,input("enter the number: ").split(" ")))]
# )
# # t[2][2][0]=10
# print(t)
 
# #None values passing onside tuple
# v1=print()
# v2=(None,None)
# print(v1,v2)
 
# #printing type =>error
# v1=print()
# v2=tuple(type(v1))
# print(v1," ",v2)
 
# #type(type()) =>error
# v1=print()
# v2=type(type(v1))
# v3=tuple(v2,)
# print(v1," ",v2,v3)


# #dynamic allocation:unpacking
# # a,b,c=((input("1st :"),input("2nd :"),input("3rd :"))
# # a,b,c=map(int,input("numbers:").split(" "))
# a,b,c=1,2,input("3rd: ")
# print(a,b,c)

# #duplicates available ,need to find which index of min value is printed
# t=(1,3,2,1)
# print(t.index(min(t)))  
# print(t.count(min(t))) #count


#advanced tuple

# # assignment 
# t1=(1,2,3)
# l=list(t1)
# print(l)

# #unpacking using *  :
# t=(1,2,3,4,5,6,7,8,9,10)
# a,*b,c=t
# print(a,b,c)

# #without split how can u assign multiple values to tuple ???
# t=input("enter the numbers: ")
# a,*b,c=t.split()
# print(type(t))
# print(a,b,c)

# #tuple does not support  split() => error
# t=tuple(input("enter the numbers: "))
# a,*b,c=t.split()
# print(type(t))
# print(a,b,c)

# t=tuple(input("enter the numbers: "))
# *a,= t  
# print(len(a))
# print(type(a))  #list
# print(a[0])


#quiz demo 01
# a=(1,2)
# print(a)

# (a,(b,c))=(1,(2,3))
# print(c)

#get() =>to access,keys() => to display keys , values () => to display values
# dict_name={
#     1:"email",
#     2:"sathya"
# }
# print(dict_name.get(2))
# print(dict_name.keys())
# print(dict_name.values())

# #duplicate keys =>override with
# d={
#     1:"ABC",
#     2:"XYZ",
#     1:"MNO"
# }
# print(d)

# #quiz 02 demo
# d={
#     1:'A',
#     True :'B',
#     1.0 :'C',
#     2:"w"
# }
# print(d.values())

# d=dict(
#     ((1,2),(3,4))
# )
# print(d)

# #example of id()
# #o/p
# #1951305064640
# #1951305064640
# v1=[5]
# v2=[5]
# print(id(v1))
# print(id(v1))


# #140723359990824
# #140723359990824
# v1=5
# v2=5
# print(id(v1))
# print(id(v1))

# #adding
# d={
#     1:'A',
#     2:"w"
# }
# d[3]=input("Enter letter: ")
# d[4]='z'
# d[5]=print()
# print(d)

# #update
# d={
#     1:'A',
#     2:"w"
# }
# d[2]=input("Enter letter: ")
# print(d)

# #delete
# d={
#     1:'A',
#     2:"w",
#     3:'q',
#     4:'r',
#     1:''
# }
# del d[1]
# d.pop(2)
# print(d)
