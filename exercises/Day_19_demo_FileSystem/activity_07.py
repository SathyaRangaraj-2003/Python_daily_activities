#activity_07:

with open("story.txt",'r') as file:
    line_count = 0
    for i in file:
        line_count += 1

print("Number of lines in text file : ",line_count)
