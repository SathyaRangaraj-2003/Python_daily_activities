#activity_09
#return mean of any number of values
#design average(*scores)

def average(*scores):
    sum = 0
    for item in scores:
        sum += item
    avg = sum /len(scores)
    return avg


print(average(10,20,30,40))

#scores = (10,20,30,40)
# print(average(*scores))
