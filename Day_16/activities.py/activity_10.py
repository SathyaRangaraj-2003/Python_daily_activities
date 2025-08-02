#activity_10:

#redesign f(x, lst=??)so:
# each call gives fresh list

def f(x, lst=list()):
    lst.append(x)
    return lst
print(f(1))
print(f(2))