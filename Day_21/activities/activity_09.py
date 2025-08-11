#activity_09:

import os

items = os.listdir('.')
print(f"Total items in {os.getcwd()} : {len(items)}")