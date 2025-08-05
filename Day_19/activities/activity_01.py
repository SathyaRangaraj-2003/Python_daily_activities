#activity_01:

from math import pi,floor
radius = int(input("Enter the circle radius: "))

print("Diameter:", 2 * radius)
print("Circumference:", floor(2 * pi * radius))
print("Area:", floor(pi * (radius **2)))