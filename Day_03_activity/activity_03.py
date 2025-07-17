
# qn:03 . Convert Boolean to Integer Without Casting Scenario: Given a boolean x = True, how do you print 1 for True and 0 for False, without using int() or type conversion?


# soln 1:
x = True
print(x * 1)  
x = False
print(x * 1)  

# soln 2:
x = True
print(x + 0)  
x = False
print(x + 0) 