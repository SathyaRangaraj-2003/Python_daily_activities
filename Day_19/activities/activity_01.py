#activity_01:

import random
def flip_biased_coin():
	if random.random() <= 0.7:
		print("Heads")
	else:
		print("Tails")
		
flip_biased_coin()