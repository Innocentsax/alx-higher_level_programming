#!/usr/bin/python3
"""Module that defines a square object"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines a square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Method that initialized the square
        Args:
           size: side's size of the square
           x: Position on x axis.
           y: Position on y axis.
        Return:
           Always nothing.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Method that returns a string"""
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                  self.width))

    @property
    def size(self):
        """Getter the size of the square
        """
        return self.width

    @size.setter
    def size(self, value):
        """Setter the size of the square
        Args:
           value: Size to assign
        Return:
           Always Nothing
        """
        self.width = value
        self.heigth = value

    def update(self, *args, **kwargs):
        """Method that update arguments for square object
        Args:
           *args: list of arguments.
           **kwargs: Dictionary of the arguments.
        Return:
           Always nothing
        """
        dict_order = ['id', 'size', 'x', 'y']
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
        """Method that returns the dictionary
           representation of a Square.
        """
        dict_order = ['id', 'x', 'size', 'y']
        dict_attrs = {}
        for key in dict_order:
            dict_attrs[key] = getattr(self, key)
        return dict_attrs
