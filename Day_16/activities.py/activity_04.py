#activity_04:

#secret number between 1 and 100 using random.randint(1,100)

import random

secret_num = random.randint(1,100)

while True:
	guess = int(input("Guess number: "))
	if guess == secret_num :
		print("Correct!")
		break
	elif guess < secret_num:
		print("Too low")
	else:
		print("Too high")