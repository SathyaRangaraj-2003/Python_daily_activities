#activity_13:

data = [[1, 2, None], [], [3, '', 4], [0, 5, 5], [None, 6]]

val = (None, '', 0, [], False)

s = {x for item in data for x in item if x not in val }
print(list(s))


# soln 2:
s = [x for item in data for x in item if x  ]
res = list(dict.fromkeys(s))
print(res)
