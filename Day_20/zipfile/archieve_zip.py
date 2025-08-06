import zipfile

with zipfile.ZipFile('archieve.zip',mode = 'w') as zf:
    zf.write('file_01.txt')
    zf.write('file_02.txt')
    zf.write('file_03.txt')