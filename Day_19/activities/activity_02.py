
#activity_02:

import random
participants = ["Michael", "Jim", "Pam", "Dwight", "Angela"]

assigned_santa = []
i=0
while True:
	secret_santa = random.choice(participants)

	if secret_santa != participants[i]  and secret_santa not in assigned_santa :
		print(f"{participants[i]} -> {secret_santa}")
		assigned_santa.append(secret_santa)
		i+=1

	if i == len(participants) :
		break



'''
import random
participants = ["Michael", "Jim", "Pam", "Dwight", "Angela"]
for item in participants:
	if item != random.choice(participants):
		print(f"{item} -> {random.choice(participants)}")
'''

#participants = ["Michael", "Jim", "Pam", "Dwight", "Angela"]
#l=random.shuffle(participants)
#print(participants)