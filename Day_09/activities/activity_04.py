#to merge into new dictionary

#declaring two dictionary
d1={
    "name" : "Ravi",
    "Age" : 25
}
d2={
    "Age" : 30,
    "city" : "Chennai"
}

#merging into new dictionary
d3=d1 | d2

#printing the final 
print(d3)

#soln 2:
d4={**d1 , **d2}
print(d4)