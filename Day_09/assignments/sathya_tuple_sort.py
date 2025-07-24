#list of tuples
data = [
    ('A', 1, 2),
    ('B', 3),
    ('C', 4, 5, 6),
    ('D',),
    ('E', 7, 8)
]
 
#sorting entire list
# key parameter to specify a function (or other callable) to be called on each list element prior to making comparisons.
sorted_data = sorted(data,key=len)

# to extract first elements
result = list(list(zip(*sorted_data))[0])
 
print(result)

