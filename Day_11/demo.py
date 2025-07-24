# #difference

# s1={1,2,3,4}
# s2={3,5,6,7}
# print(s1.difference(s2))

# #symmetric_difference
# s1={1,2,3}
# s2={3,4,5}
# s1.symmetric_difference_update(s2)
# print(sorted(s1))

# x=set()
# y={1,2}
# z=x^y
# print(type(z),len(z))

# a={1,2,3}
# b=a
# print(id(b),id(a))  #same id


# # relationship based operations
# A={1,2,3}
# B={1,2,3,4,5,6}
# C={1,2}
# print(A.issubset(B))  #true
# print(C <= A) #true

# print(A < B) #true
# print(B < C) #false

# #frozenset
# a=set()
# b={frozenset()}
# c={
#     frozenset(),
#     frozenset({1})
# }
# print(b.issubset(c))  #true

# d={
#     {1,2,3} : "set as key"
# }
# print(d) #error

# ns={
#     {1,2},{3,4}
# }
# print(ns) #error

# d={
#     frozenset([1,2]):"frozen"
# }
# print(d)

# ns={
#     frozenset([1,2]),
#     frozenset([3,4])
# }
# print(ns) #true

