num=input().split(" ")
num_character=num[1::3]
reversed=num_character[::-1]
message=""
for val in reversed:
    message+=chr(int(val))
print(message)