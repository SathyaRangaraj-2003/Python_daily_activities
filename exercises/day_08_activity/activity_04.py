#activity 04

#declaring
fruit_prices = {
'elppa' : 100,
'ayapap' : 80,
'egnaro' : 60
}

#user input
fruit=input("Enter the fruit name :") #apple i need to return 100

print(fruit_prices.get(fruit[::-1]))