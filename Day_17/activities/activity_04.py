#activity_04:

#password checker
def password_check(password):
	letters = False
	is_upper = False
	is_lower = False
	is_digit = False
	is_special = False
	special_characters = "!@#$%^&*()+=-_[]{}|;:',.<>?/`~"
	for chr in password:
		if chr.isupper():
			is_upper = True
		if chr.islower():
			is_lower = True
		if chr.isdigit():
			is_digit = True
		if chr in special_characters:
			is_special = True
	if len(password) >= 8:
		letters = True
	strength = sum([letters + is_upper + is_lower + is_digit + is_special])
	
	if 1 <= strength <= 2:
		return "Weak"
	elif 3 <= strength <= 4:
		return "Moderate"
	else:
		return "Strong"
password = input("Enter the password : ")
print(password_check(password))