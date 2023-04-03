#!/usr/bin/python3
Rectangle = __import__('3-rectangle').Rectangle

rect = Rectangle(2, 4)
print("Area: {} - Perimeter: {}".format(rect.area(), rect.perimeter()))

print(str(rect))
print(repr(rect))

print("--")

rect.width = 10
rect.height = 3
print(rect)
print(repr(rect))
