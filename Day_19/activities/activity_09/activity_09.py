#activity_09:

quote = "Don't be afraid to fail"

with open('quote.txt','a') as file:
	file.write(quote + "\n")
	
print(open('quote.txt').read())