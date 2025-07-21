#activity 04 
#scrammpled words i need a value

#declaring
fruit_prices = {
'elppa' : 100,
'ayapap' : 80,
'egnaro' : 60
}

#user input
fruit=input("Enter the fruit name :") 

#getting value
print(fruit_prices.get(fruit[::-1]))