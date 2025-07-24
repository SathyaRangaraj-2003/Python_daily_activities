
#given 4 sets
A = {1, 2, 3, 4, 5}
B = {3, 4, 5, 6, 7}  
C = {5, 6, 7, 8, 9}
D = {1, 3, 7, 9, 10}

# Find elements that appear in exactly in sets out of these 4 sets.
# pairwise = (A&B)|(A&C)|(A&D)|(B&C)|(B&D)|(C&D)
# three_common = (A&B&C)|(A&B&D)|(A&C&D)|(B&C&D)
# print("Elements in exactly 2 sets:",pairwise ^ three_common)

print("Elements in exactly 2 sets:",((A&B)|(A&C)|(A&D)|(B&C)|(B&D)|(C&D)) ^ ((A&B&C)|(A&B&D)|(A&C&D)|(B&C&D)))
