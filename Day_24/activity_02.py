#activity_05:

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return f"Circle: {math.pi * self.radius ** 2}"

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return f"Rectangle: {self.width * self.height}"

class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return f"Triangle: {(1/2) * self.base * self.height}"

def print_area(shape):
    print(f"Area of {shape.area()}")


print_area(Circle(3))
print_area(Rectangle(2, 4))
print_area(Triangle(3, 7))
