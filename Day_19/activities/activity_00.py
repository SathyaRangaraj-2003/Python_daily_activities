#activity_00:

from math import pi,floor,ceil
radius = int(input("Enter the circle radius: "))

print("Diameter:", 2 * radius)
print("Circumference:", floor(2 * pi * radius))
print("Area:", ceil(pi * (radius **2)))