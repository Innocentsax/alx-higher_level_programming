#!/usr/bin/python3
"""Write a base geometry class BaseGeometry"""


class BaseGeometry:
    """class represents a base geometry"""

    def area(self):
        """Not implemented yet"""
        raise Exception("area() method is not implemented")

    def integer_validator(self, name, value):
        """validates a value as an integer"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
