#to print 3rd ingredients
ingredients=["milk powder","cardamom","sugar","ghee"]
print("ingredients:",ingredients[2])

ingredients=list(map(str,input("Enter ingredients:").split(",")))
print(ingredients[2])