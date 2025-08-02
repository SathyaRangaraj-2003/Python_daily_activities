#activity_07:

nums = [4, 2, 4, 3, 2, 2]

set_nums = set(nums)
result = []

for n in set_nums:
	count = nums.count(n)
	result.append((n,count))
print(result)