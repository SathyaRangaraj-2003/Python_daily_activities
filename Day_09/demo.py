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
d = {
    1 : 'orgean',
    2 : 'appel',
    3 : 'jacfruitk'
}

sorted_keys = dict(zip(map(''.join, map(sorted,d)), d))

print(d.get(sorted_keys.get(''.join(sorted(input("Enter fruit name:")))),
 "Fruit not found"))

# user_input=input("Enter the string to get id: ")

# d2=dict(list(map(sorted,user_input)))
# print(d2)



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

# #values
# d = {
#     'x' : 10,
#     'z' : 30
# }
# value_view=d.values()
# d['y']=20
# print(list(value_view)) #10,30,20


# #guess o/p

# config = {}
# result = config.setdefault('database', {}).setdefault('connections', [])
# result.extend(['mysql', 'postgres'])
# config.setdefault('database', {}) ['port'] = 5432
# print(len(config['database']), len(result))


# # quiz demo

# # pop() and popitem()
# d={
#     'a':10,
#     'b':20
# }
# x=d.pop('b',3)
# print(x)

# z=d.pop('c',3)
# print(z)

# #popitem()
# d={
#     'a':10,
#     'b':20
# }
# d.popitem()
# print(d)

# d={
#     'a':10,
#     'b':20
# }
# d.pop('a')
# print(d['a'])  #=>error


# d={
#     'a':10,
#     'b':20
# }
# d2=d
# d.clear()
# print(len(d2))  #o/p =>0 main reference even deleted so an


# d={
#     'a':10,
#     'b':20
# }
# v=list(d.values())
# v.append(3)
# print(len(d))


# d=((10,20),(30,40,50),(60,70))
# (a,b) ,(c,*rest), (d,e)=d
# print(a+c+d,len(rest))

# d=({'count'  : 5},)
# res=d*2
# print(res)

# base={'user' : {'profile' : {'name' : 'John'}}}
# update_data= {'user' : {'profile' : {'age':25},
#               'setting' : {'theme' :'dark'}}}

# base['user'].update(update_data['user'])
# print(base['user']['profile'])  #{'age' :25}


