#activity_10

with open("original.txt", "r") as in_file:
    lines = in_file.readlines()
reversed_lines = reversed(lines)  
with open("reversed.txt", "w") as out_file:
    out_file.writelines(reversed_lines)