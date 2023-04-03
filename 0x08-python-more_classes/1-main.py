#!/usr/bin/python3
Rectangle = __import__('1-rectangle').Rectangle

rect = Rectangle(2, 4)
print(rect.__dict__)

rect.width = 10
rect.height = 3
print(rect.__dict__)
