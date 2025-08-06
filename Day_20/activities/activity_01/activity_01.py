#activity_01

import zipfile
zip_path = input("Enter the path : ")
with zipfile.ZipFile(zip_path,'r') as file:
    if 'foo.txt' in file.namelist():
        print("Found!")
    else:
        print("Missing!")