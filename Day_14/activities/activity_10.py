#activity_10:

#2-string ,print "match" if they are equal (case insensitive) else "no match"
#one if-statement(no ternary)

str1 = input("Enter the String 1 : ")
str2 = input("Enter the String 2 : ")

if str1.upper() == str2.upper():
	print("Match")
else:
	print("No match")