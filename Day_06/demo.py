# l=[1,2,"raja"]
# print(l.sort())

# #collection of all datatype
# sathya_tuple=("apple",2,None,True,5.9,[1,2],5+8,1>>2,3>8)
# print(sathya_tuple)

# # list
# list=[1,2,3,4]
# tuple=(list[0:3])
# print(tuple)

# t1=(1,2,3,4,5)
# print(t1)

# #tuple by list
# list=tuple([1,2,3,4])
# tuple=(list[0:3])
# print(tuple)

# #tuple with list
# x=tuple([1,2])
# print(x)

# #nested tuple
# x=((1,2),(3,4))
# print(x[0])

# #nested tuple by negative indexing
# x=((1,2),(3,4))
# print(x[-1][-2])
# t1=1,2,3
# t2='a','b'
# t3=t1+t2
# print(t3*3)

# # try =>to print index of all occurance
# t=(3,2,4,2)
# print(t[:].index(2) + t[1:].index(2))

# #try circulate values
# t=(10,20,30,40,50)
# print(t[:] + t[1:] + t[2:] + t[3:] + t[4:])

# #min=>error
# t=(
#     2,4,1,(0,3)
# )
# print(max(t))

# #del tuple_name =>to delete entire tuple
# t=(10,20,30)
# del t
# print(t)


# #bank details
# #accinfo=acc_no,name,pan,balance,credit,debit
# acc_info=(100,"sathya","PAN3420",[1000,500,900])
# amount_debit=int(input("Enter amount :"))
# amount_credit=int(input("Enter amount :"))
# acc_info[3][0]-=amount_debit
# acc_info[3][2]-=amount_debit
# acc_info[3][1]+=amount_credit
# print(acc_info)


# #accinfo=acc_no,name,pan,balance,credit,debit
acc_info=(100,"sathya","PAN3420",[1000,],input("Enter credit or debit:"))

acc_info[3][0]=((acc_info[4]=='credit' and acc_info[3][0]+int(input("Enter credit amount :")) ) or (acc_info[4]=='debit' and acc_info[3][0]-int(input("Enter debit amount :"))))

print(acc_info)
