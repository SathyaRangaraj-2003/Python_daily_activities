#activity_07:

line_count = 0
with open("story.txt",'r') as file:
    for i in file:
        line_count += 1

print("Number of lines in text file : ",line_count)




#Using .read() or .readlines() will load entire file to memory