#activity_16:

val1 , val2 ,val3=input("Enter 3 booleans : ").split(",")
print("Exactly one" if [val1,val2,val3].count("True") == 1 else "Nope")