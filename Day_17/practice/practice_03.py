'''
Write a  program or function that validates user password with the following requirements:
Password ≠ username
Password ≠ first name or last name
At least 10 characters
Must be alphanumeric (letters and numbers)
Must include both uppercase and lowercase letters'''


#acitivity_03:

user_name = input("Enter the user name: ")
first_name = input("Enter the first_name: ")
last_name = input("Enter the last_name: ")

password = input("Enter the password :")

if len(password) >= 10:
	if password != user_name and (password != first_name or first_name != last_name):
		for chr in password:
			if not chr.isalnum() and  ( not chr.isupper() or not chr.islower()):
				print("Enter the correct password")
				break
		else:
			print("password correct")
		
else:
	print("Enter the correct password")