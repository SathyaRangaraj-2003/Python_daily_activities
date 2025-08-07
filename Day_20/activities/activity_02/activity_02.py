#activity_02:

'''
import zipfile

with zipfile.ZipFile('activity_02.zip','w') as zf:
    zf.write('file_01.txt')
    zf.write('file_02.txt')
    zf.write('file_03.txt')
    zf.extractall()
    print(zf.namelist())
'''

import zipfile

with zipfile.ZipFile('activity_02.zip','w') as zf:
	zf.write('file_01.txt')
	zf.write('file_02.txt')
	zf.write('file_03.txt')

for i in range(1,4):
	with open('file{i}.text','w') as f:
		f.write(f"Hello from file {i}")

with zipfile.ZipFile('activity_02.zip','r') as zf:
	zf.read(file0.txt)