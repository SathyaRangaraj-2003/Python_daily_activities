#insertion sort:

arr = [23,1,10,5,2]

for i in range(1,len(arr)):
	j=i
	while j>0 and arr[j-1] > arr[j]:
		arr[j] , arr[j-1] = arr[j-1] , arr[j]
		j =j-1
print(arr)