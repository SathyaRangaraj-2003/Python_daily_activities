#create string variables
data="Luna42Kai3.14True#Knight"
#Extract "Luna" and convert it to uppercase
name=data[0:4].upper()
#Extract the number 42 
add=int(data[4:6])
#Extract the float value 3.14 
multiply = float(data[9:13])
#Slice "Knight" using negative indexing and reverse it.
slice=data[-1:-7:-1]
#print
print("Name: "+name)
print(f"{add} + 8 =",add+8  )
print(f"{multiply} * 2 =",multiply*2)
print("Reversed Title: "+slice)