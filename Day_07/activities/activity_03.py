
#jugs mugs pugs,jugs mugs,jugs mugs,mugs pugs,jugs(3),mugs(5),pugs(7) => 7 combination

num = int((v1 := input("Enter the number: ")).isdigit() and v1 or input("Enter numeric value: "))
print((num % 3 == 0 and num % 5 == 0 and num % 7 == 0 and "jugs mugs pugs") or (num % 3 == 0 and num % 5 == 0 and "jugs mugs") or (num % 3 == 0 and num % 7 == 0 and "jugs pugs") or (num % 5 == 0 and num % 7 == 0 and "mugs pugs") or (num % 3 == 0 and "jugs") or (num % 5 == 0 and "mugs") or (num % 7 == 0 and "pugs") or num)