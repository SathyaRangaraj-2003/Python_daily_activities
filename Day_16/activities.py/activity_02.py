#activity_02
#binary search

data = [10,20,30,40,50,60]
target = 20

low = 0
high = len(data) - 1

while low <= high :
    mid = (low + high) // 2
    if data[mid] == target:
        print("Found the target")
        break
    elif data[mid] < target:
        low = mid + 1
    else:
        high = mid - 1
else :
    print("Not Found..")