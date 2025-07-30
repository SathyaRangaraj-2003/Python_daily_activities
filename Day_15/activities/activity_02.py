
#activity_02


#soln 1:
str = input("enter the string :")

count = 0
for chr in str.lower():
	if chr == 'a' or chr == 'e' or chr == 'i' or chr == 'o' or chr == 'u':
		count+=1
print(count)


#soln 2:
str = input("enter the string :")

count = 0
for chr in str.lower():
	if chr in ['a','e','i','o','u']:
		count+=1
print(count)


#soln 3:
str = input("enter the string :")
vowels ="aeiou"

count = 0
for chr in str.lower():
	if chr in vowels:
		count+=1
print(count)