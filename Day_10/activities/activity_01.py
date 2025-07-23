#update list
#print how many names were actually added.

#declaration of set
students ={ 'Alice' , 'Bob' , 'Charlie' }
new_entries = ['Charlie' ,'Diana' ,'Eve' , 'Bob' ,'Frank']

#getting size before update
original=len(students)

#adding all names to students set
students.update(new_entries)

#printing how many names were actually added.
# print(students)
print(len(students)-original)