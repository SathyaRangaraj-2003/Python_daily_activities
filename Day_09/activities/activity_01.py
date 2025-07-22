
#merge 2 dictionaries 
#o/p : 
# {
#     'x' : 10,
#     'y' : 99,
#     'z' : 30
# }


dict1 = {
    'x' : 10,
    'y' : 20,
}
dict2 = {
    'y' : 99,
    'z' : 30,
}
dict1.update(dict2)
print(dict1)


print(dict1 | dict2)

print({**dict1 , **dict2})  #return new dictionary keyword argument