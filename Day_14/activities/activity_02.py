#inputs

user_name =  input("Enter the username : ")
password = input("Enter the password : ")

if user_name == "admin" and (password == "secret123" or password == "letmein" ):
	print("Granted..")