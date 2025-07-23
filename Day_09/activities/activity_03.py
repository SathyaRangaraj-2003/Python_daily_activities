#print matching name eve key is reversed
#tuple can be key

#declaring
access_data={
    (103,209) : "Alice",
    (104,210) : "Bob",
    (105,211) : "Charlie",
    (106,212) : "Diana"
}

#user biometric ids input
auth_input=tuple(map(int,input("Enter the two ids: ").split(",")))

#printing matching name eve key is reversed
print(access_data.get(auth_input) or access_data.get(auth_input[::-1]))
#or
print(access_data.get(auth_input) or access_data.get((auth_input[1],auth_input[0])))


# input = map(int,input("Enter the two ids: ").split(","))
# print(input)