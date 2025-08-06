#activity_02:

import zipfile

with zipfile.ZipFile('activity_02.zip','w') as zf:
    zf.write('file_01.txt')
    zf.write('file_02.txt')
    zf.write('file_03.txt')
    print(zf.extractall())