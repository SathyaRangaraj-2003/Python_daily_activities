

# #comparison operators #activity_00
# #  <,>,==,<=,>=,!=

a=5
b=10
print(a == b,a != b,a < b,a > b,a <= b,a >= b)
print(id(a),id(b), id(a) == id(b) )

c=int(True)
d=1
print(c == d , id(c) == id(d))

e=5
f="5"
print(e,f,e == f)  #exact pattern (str == int) is possible
print(5.0 == 5) #True takes numerical value equal

d={}
d2={}
print(d == d2)

t1=([])
t2=([])
print(t1 ==  t2) #true

a=12
b=10
print(a != b,5.0 != 5, 5.0 < 5.1,5.0 <= 5.1 , 4.99 <= 4.9999)

print('5'> 3) #error  (str > int) is not possible

print("Hello" == "hello")  #False
print("Hello" == "Hello")  #True
print("apple" < "banana")  #True
print("zebra" > "apple")   #True
print("cat" > "elephant")  #False

password ="secret123"
print(len(password) >= 8)  #True

print("elephant" > "elephant") #False
print("elephant" > "Elephant") #True 101 > 69
print(chr(97))