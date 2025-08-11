#activity_10

import os

path = os.path.join("project","assets","images")
os.makedirs(path,exist_ok = True)
print(f"Directory {path} is created inside current directory")