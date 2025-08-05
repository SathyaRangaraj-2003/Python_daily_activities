
try:
    file = open('hello.txt', 'r')
    content = file.read()
    print(content)
except:
    print("File not found")