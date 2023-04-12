#!/usr/bin/python3
"""Write a function that writes a string to a text file (UTF8) and returns the number of characters written
"""


def read_file(filename=""):
    """Print the contents of a UTF8 text file to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
