
#step 1:get user_name 
#step 2:then input in lower case.
#step 3:converted to upper case without string upper().

user_name=input("Enter your name:")
lower_case_name=user_name.lower()
upper_case_name=chr(ord(lower_case_name)-32)
print("Returning name in upper case :",upper_case_name)


# crt soln :
user_name = input('Enter your name: ').lower()
resulting_name = ""
resulting_name+=chr(ord(user_name[0])-32)
resulting_name+=chr(ord(user_name[1])-32)
resulting_name+=chr(ord(user_name[2])-32)
resulting_name+=chr(ord(user_name[3])-32)
resulting_name+=chr(ord(user_name[4])-32)
resulting_name+=chr(ord(user_name[5])-32)
resulting_name+=chr(ord(user_name[6])-32)
print(resulting_name)