
#jugs mugs

num = int((v1 := input("Enter the number: ")).isdigit() and v1 or input("Enter numeric value: "))
print((num % 3 == 0 and num % 5 == 0 and "jugs mugs") or (num % 3 == 0 and "jugs") or (num % 5 == 0 and "mugs") or num)