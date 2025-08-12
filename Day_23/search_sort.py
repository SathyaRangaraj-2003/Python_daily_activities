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






