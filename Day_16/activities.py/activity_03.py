#activity_03
#selection_sort


#soln 1:
a = [5,4,2,1,6,3]

for i in range (0,len(a)-1):
	m = i
	for j in range (i+1,len(a)):
		if a[m] > a[j]:
			m = j
	a[i] , a[m] = a[m] , a[i]
print(a)

#by list,methods



#soln 2:
a = [5,4,2,1,6,3]

for i in range (0,len(a)-1):
	m = i
	for j in range (i+1,len(a)):
		if a[m] > a[j]:
			m = j
	temp = a[i]
	a[i] = a[m]
	a[m] = temp
print(a)