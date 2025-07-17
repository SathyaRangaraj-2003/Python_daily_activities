
#ascii number to character
v1,v2,v3=map(int,input("Enter three ascii numbers with spaces:").split(' '))
print(f"char 1:{chr(v1)}\nchar 2:{chr(v2)}\nchar 3:{chr(v3)}")  #chr(int())


v1,v2,v3=input("Enter three ascii numbers with spaces:").split(' ')
print(f"person 1:{chr(int(v1))}\nperson 2:{chr(int(v2))}\nperson 3:{chr(int((v3)))}")