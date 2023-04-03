#!/usr/bin/python3
Rectangle = __import__('2-rectangle').Rectangle

rect = Rectangle(2, 4)
print("Area: {} - Perimeter: {}".format(rect.area(), rect.perimeter()))

print("--")

rect.width = 10
rect.height = 3
print("Area: {} - Perimeter: {}".format(rect.area(), rect.perimeter()))
