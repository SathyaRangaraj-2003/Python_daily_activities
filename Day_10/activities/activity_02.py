#one-liner that finds elements common to all sublists
#intersect

#list of lists
l1=[[1,2,3,4],[2,3,4,5],[3,4,5,6],[4,5,6,7]]

# one-liner that finds and prints elements common to all sublists

ele= list(set.intersection(*map(set, l1)))
print(ele)


# print(list(set(l1[0]) & set(l1[1]) & set(l1[2]) & set(l1[3])))