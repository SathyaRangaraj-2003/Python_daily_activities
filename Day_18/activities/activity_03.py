#activity_03:

nums = [1,2,3,4,5]
print(list(map(lambda x : x**2 ,filter(lambda x : x%2==0, nums))))