file = open('hello.txt', 'r')
content = file.read()
print(content)
file.close()


try:
    file = open('hello.txt', 'r')
    content = file.read()
    print(content)
    file.close()
except Exception as e:
    print(e)