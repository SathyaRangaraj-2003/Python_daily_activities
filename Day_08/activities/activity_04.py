# #activity 04 
# #scrammpled words :  display a value => anagram

# #soln 01:
# #declaring
# fruit_prices = {
# 'elppa' : 100,
# 'ayapap' : 80,
# 'egnaor' : 60
# }
# #user input
# fruit=tuple(sorted(input("Enter the fruit name :")) )
# print(fruit_prices.get(fruit[::-1]))


# #soln 02:
# #declaring
# fruit_prices = {
# 'elppa' : 100,
# 'ayapap' : 80,
# 'egnaor' : 60
# }
# #sorted keys
# fruit_dict={
# tuple(sorted(k)):v
# for k,v in fruit_prices.items()
# }

# #user input
# fruit=tuple(sorted(input("Enter the fruit name :")) )
# #getting the value
# print(fruit_dict.get(fruit,"Fruit not found.."))


# #soln 3:
# # declaring
# fruit_prices = {"alpep": 100, "egnaro": 80, "ananab": 60}

# #user input
# fruit_name = input("Enter fruit name:")

# key = list(fruit_prices)[list(map(sorted, fruit_prices)).index(sorted(fruit_name))]
# print(fruit_prices[key])



# soln 04:  
#declaring
fruit_prices = {"alpep": 100, "egnaro": 80, "ananab": 60}

#new dictionary
sorted_keys = dict(zip(map(''.join, map(sorted, fruit_prices)), fruit_prices))

#display a value
print(fruit_prices.get(sorted_keys.get(''.join(sorted(input("Enter fruit name:")))),
 "Fruit not found"))


