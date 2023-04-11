#!/usr/bin/python3
"""Write a class MyInt that inherits from int."""


class MyInt(int):
    """Invert int operators == and !=."""

    def __eq__(self, value):
        """Replace == opeartor with != behavior."""
        return self.real != value

    def __ne__(self, value):
        """Replace != operator with == behavior."""
        return self.real == value
