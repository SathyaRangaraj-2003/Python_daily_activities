#activity_03

import zipfile

with zipfile.ZipFile('activity_03.zip','w') as zf:
	zf.write('file1.txt')
	zf.write('file2.txt')
	zf.write('file3.txt')


with zipfile.ZipFile('activity_03.zip','r',compression = zipfile.ZIP_BZIP2) as zf:
	for info in zf.infolist():
		print(f"{info.filename} => {info.compress_size} bytes")
	

'''
#activity_03

import zipfile

with zipfile.ZipFile('activity_03.zip','w') as zf:
	zf.write('file1.txt')
	zf.write('file2.txt')
	zf.write('file3.txt')


with zipfile.ZipFile('activity_03.zip','r',compression = zipfile.ZIP_BZIP2) as zf:
	for file_name in zf.namelist():
		print(f"{file_name} => {zf.getinfo(file_name).file_size} bytes")
'''			

# with zipfile.ZipFile('activity_03.zip','r',compression = zipfile.ZIP_BZIP2) as zf:
# 	print(zf.infolist())
# 	print(zf.namelist())
# 	print(zf.getinfo('file1.txt'))