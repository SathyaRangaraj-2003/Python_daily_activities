# #try 01:reverse the dictionary ,
# # the value should be a key and key shoud turn to value

# d={
#     (103,209) : "Alice",
#     (104,210) : "Bob",
#     (105,211) : "Charlie",
#     (106,212) : "Diana"
# }
# new_dict=dict(zip(d.values(),d.keys()))
# print(new_dict)

# s={}
# print(type(s))  #dict

# s1={1,2}
# s2={3,4}
# print(id(s1),id(s2)) #id differ

#hashable => int,str,tuple,float,complex
# s={1,2,[5,6],(2,3),30.988,True,{1:'a'}}  #list,dict,nested set is not accepted in set

# s={(2,3),"sathya",30.988, 3+4j ,True}  #bool accepted but it is not displayed in o/p if (1,0) in set
# print(s)

# #guess
# word=set('programming,programming')
# # word=set(('programming','programming'))
# print(word)
# print(len(word))


#qn 02:set data to be same all the tym in same order 
# #adding
# s={'apple','banana'}
# s.add('orange')
# print(s)

#  #update
# s={'apple','banana'}
# # s.update('orange')
# s.update(['abc','xyz'])
# s.update((123,456))
# s.update({1:'a'})
# print(s)


#try 03: print how many names were actually added.
#if scenario of class have same name with same initial =>2 person how will you add in set
#declaration of set

# #soln 1
# from collections import Counter

# students =Counter(['Alice' , 'Bob' , 'Charlie' ]) 
# new_entries = ['Charlie' ,'Diana' ,'Eve' , 'Bob' ,'Frank']

# students.update(new_entries)
# print(type(students))

# print(students)

# #declaration of set
# students ={ 'Alice' , 'Bob' , 'Charlie' }
# new_entries = ['Charlie' ,'Diana' ,'Eve' , 'Bob' ,'Frank']

# #getting size before update
# original=len(students)

# #adding all names to students set
# students.update(new_entries)
# print(students)

# #pop =>randomly 
# s={'apple','banana','abc'}
# s.pop()
# print(s)

# #membership in,not in
# c={'r','g','b'}
# condition={'r' not in c,'g' in c,'r' in c}  #only one true
# print(condition)


# #quiz 
# s={"banana"} #1
# s=set("banana") #3
# print(len(s))

# s={1,2,3,(4,5)}
# print(len(s))

# s={'a','b'}
# s.update('cd',['e','f'])
# print(sorted(s))

# s={1,2,3}
# s.discard(4)
# s.pop(4) #error
# s.remove(4) #error
# print(s)


# s={'1','2'}
# s.discard('3')
# print(len(s))

# a=set()
# a.update([1],(2,),{3})
# print(len(a))

# a={1,2}
# b=a
# a.clear()
# print(b)

# a=5             #0101
# b=10            #1010
# print(a & b)    #0000
# print(a and b)

