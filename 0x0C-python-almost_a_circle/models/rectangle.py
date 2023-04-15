#!/usr/bin/python3
"""Defines a rectangle module (modules.rectangle)"""
from models.base import Base


class Rectangle(Base):
    """Defines a rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Method that init values for a rectangle object
        Args:
           width:size of the width
           height: size of the height
           x: Variable x
           y:  Variable y
        Return:
           Always nothing
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    # Getter and setter of width
    @property
    def width(self):
        """Getter the size of width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Setter the size of width
        Args:
           value: Size to assign to the width
        Return:
           Always Nothing
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    # Getter and setter of height
    @property
    def height(self):
        """Getter the size of height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Setter the size of height
        Args:
           value: Size to assign to the height
        Return:
           Always Nothing
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    # Getter and setter for x variable
    @property
    def x(self):
        """Getter of x variable
        """
        return self.__x

    @x.setter
    def x(self, value):
        """Setter of x variable
        Args:
           value: value to assign to x variable
        Return:
           Always Nothing
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    # Getter and setter for y variable
    @property
    def y(self):
        """Getter of y variable
        """
        return self.__y

    @y.setter
    def y(self, value):
        """Setter of y variable
        Args:
           value: value to assign to y variable
        Return:
           Always Nothing
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """Method that returns the area of the rectangle object
        Args:
           Not arguments
        Return:
           Area of the rectangle object
        """
        return self.width * self.height

    def display(self):
        """Method that prints to stdout
           Rectangle object with the character #
        """
        for i in range(self.y):
            print()
        for i in range(self.height):
            print(" " * self.x + self.width * '#')

    def __str__(self):
        """Method that override str method
        """
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x,
                                                        self.y, self.width,
                                                        self.height))

    def update(self, *args, **kwargs):
        """Method that changed the order of arguments for rectangle object
        Args:
           *args: list of arguments
           **kwargs: Dictionary with arguments
        Return:
           Always nothing
        """
        dict_order = ['id', 'width', 'height', 'x', 'y']
        if args is not None and bool(args) is True:
            i = 0
            for key in dict_order:
                try:
                    setattr(self, key, args[i])
                except IndexError:
                    pass
                i += 1
        else:
            for key in dict_order:
                try:
                    setattr(self, key, kwargs[key])
                except KeyError:
                    pass

    def to_dictionary(self):
        """Method that returns a dictionary with
           attributes of the object.
        """
        dict_order = ['x', 'y', 'id', 'height', 'width']
        dict_attrs = {}
        for key in dict_order:
            dict_attrs[key] = getattr(self, key)
        return dict_attrs
