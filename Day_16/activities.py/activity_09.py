#activity_09
#return mean of any number of values
#design average(*scores)

def average(*scores):
    avg = sum(scores) /len(scores)
    return avg


print(average(10,20,30,40)) 
#if no score 

#scores = (10,20,30,40)
# print(average(*scores))
