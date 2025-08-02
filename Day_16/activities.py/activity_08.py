
#activity_08:
#function that can be used instead of sum()

a = (1,2,3,4,5)

def add(a):
    sum = 0
    for item in a:
        sum +=item
    return sum
print(add(a))