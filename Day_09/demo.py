# #guess o/p 
# d = {
#     'x' : 10,
#     'y' : 20,
# }
# d['z']=30

# print(d.items())  #group of tuple inside a list
# print(type(d['x']))  #int is datatype of 'x' value
# print(d.pop())  #pop() default is not working
# print(d.pop('z'))   #always it should with keys inside pop()
# print('x' in d)  #membership =>in ,not in works for both keys,values.
# print(10 in d.values())


# #try 01: if the value is scrambled how can u perform in membership operators
# d = {
#     'x' : 10,
#     'y' : 'appel',
#     'z' : 30
# }
# print(map'apple' in d.values())


# #list of dictionary is possible
# d=[
#     {'a' : 1, 'b' :2}
# ]
# print(d)

# #nested dictionary
# students={
# "Anita" : {"Math" : 95 , "Science" : 89},
# "Ravi" : {"Math" : 80 , "Science" : 92},
# "Pavi" : {"Math" : 88 , "Science" : 85}
# }
# print(students["Ravi"])
# print(students["Ravi"]["Science"])


# #len()
# d = {
#     'x' : 10,
#     'y' : [1,2],
#     'z' : 30
# }
# print(len(d.values()))

#values
d = {
    'x' : 10,
    'z' : 30
}
value_view=d.values()
d['y']=20
print(list(value_view)) #10,30,20