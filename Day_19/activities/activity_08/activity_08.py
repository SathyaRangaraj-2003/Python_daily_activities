
#activity_08:


quote = "Don't be afraid to fail"

with open('quote.txt','w') as file:
	file.write(quote)
	
print(open('quote.txt').read())