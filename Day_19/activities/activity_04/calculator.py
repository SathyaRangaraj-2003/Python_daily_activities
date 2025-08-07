#activity_06
#calculator.py

import mymath

a = int(input("Enter the num1 : "))
b = int(input("Enter the num2 : "))

print("Addition :", mymath.add(a,b))
print("Subtraction :", mymath.subtract(a,b))
print("Multiplication :", mymath.multiply(a,b))
print("Division :", round(mymath.divide(a,b), 2))