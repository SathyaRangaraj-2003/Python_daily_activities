#day_21

'''

data = '{"name" :[ "Alice" , "Bob"] , "Age" : [30 , 25] , "City" : ["New York" , "Bob"] }'

import json

data_json = json.loads(data)
print(data_json["name"])

print("{} hello {}".format(42,"alice"))

print("{1} hello {0}".format("alice",42))

print("{n1} hello {n2}".format(n1=42,n2="alice"))

print("{%d} Hello, {%s}!" % (42, 'Alice'))

user = "Ravi"
score = 87.5

print(f"{user=}, {score=}, {score/100 = :.2%}")

import numpy as np

a = np.array([1,2,3,4])
print(a.mean())'''

import pandas as pd
help(pd)