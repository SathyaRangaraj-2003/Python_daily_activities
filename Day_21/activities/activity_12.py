#activity_12

import os

root_path = os.getcwd()

count = 0

for dirpath,dirnames,filenames in os.walk(root_path):
	for file in filenames:
		if file.endswith('.txt'):
			print(os.path.join(dirpath,file))
			count += 1
		

print(f"Total Count: {count}")