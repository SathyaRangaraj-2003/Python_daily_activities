
#compress
# import zipfile

# with zipfile.ZipFile('demo.zip',mode = 'w') as zf:
#     zf.write('file_01.txt')
#     zf.write('file_02.txt')
#     zf.write('file_03.txt')

# #namelist(),extractall()
# import zipfile
# with zipfile.ZipFile('archieve.zip',mode = 'r') as zf:
#     zf.read('file_01.txt')
#     print(zf.namelist())
#     zf.extractall()


# import zipfile

# with zipfile.ZipFile('archieve.zip',mode = 'r') as zf:
#     zf.read('file_01.txt')


# import zipfile

# with zipfile.ZipFile('archieve.zip','r',compression=zipfile.ZIP_DEFLATED) as zf:
    



# import zipfile

# with zipfile.ZipFile('archieve.zip','r',compression=zipfile.ZIP_DEFLATED) as zf:
#     zf.extractall('archieve_zip')

import zipfile

with zipfile.ZipFile('demo.zip','r') as zf:
    print(zf.namelist() )
    file_extract = input("Enter the file to extract : ")
    zf.extract(file_extract)
