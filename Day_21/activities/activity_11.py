#activity_11

import os

starting = os.getcwd()
print(f"Starting at: {starting}")

temp_folder = os.path.join(starting,"temp_folder")

os.makedirs(temp_folder ,exist_ok = True)

os.chdir(temp_folder)

print(f"Now in: {os.getcwd()}")

os.chdir(starting)

print(f"Returned to: {os.getcwd()}")