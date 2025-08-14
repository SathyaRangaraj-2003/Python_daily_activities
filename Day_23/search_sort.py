'''
#linear search

lst = [1,5,3,7,9,2,4]

#target from user to search

target = int(input("Enter the target :"))

def linear_search(lst,target):
	for i in range(len(lst)):
		if lst[i] == target:
			return i
	return -1

print(linear_search(lst,target))



#binary search

arr = [10,40,30,20,60]

arr.sort()

target = int(input("Enter the target :"))

def binary_search(arr,target):
	l = 0
	h = len(arr) - 1
	while(l<=h):
		mid = (l+h)//2
		if arr[mid] == target:
			return mid
		elif arr[mid] < target:
			l = mid + 1
		else:
			h = mid - 1
	return -1

print(binary_search(arr,target))



#selection_sort

a = [5,4,2,1,6,3]

for i in range (0,len(a)-1):
	m = i
	for j in range (i+1,len(a)):
		if a[m] > a[j]:
			m = j
    
    if min_index != i:  # Avoid unnecessary swap
        a[i] , a[m] = a[m] , a[i]
print(a)



#insertion sort:

arr = [23,1,10,5,2]

for i in range(1,len(arr)):
	j = i - 1
	key = arr[i]
	while j>=0 and arr[j] > key:
		arr[j+1] = arr[j] 
		j =j-1
	arr[j+1] = key
print(arr)


#bubble sort:

def bubble_sort(arr):
    n = len(arr)
   
    for i in range(n):
        
        swapped = False
        for j in range(0, n - i - 1):
            
            if arr[j] > arr[j + 1]:
                
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        if not swapped:
            break
    return arr

my_list = [2,6,4,9,1]
sorted_list = bubble_sort(my_list)
print(f"Sorted list: {sorted_list}")


'''
def bubble_sort(lst):
    n = len(lst) 
    for i in range(n):
        swapped = False
        for j in range(0,n-1-i):
            if lst[j] >  lst[j+1]:
                lst[j] , lst[j+1] = lst[j+1] ,lst[j]
                swapped = True
        if not swapped:
            break
    return lst

arr =[2,6,4,9,1]
print(f"sorted array{bubble_sort(arr)}")
