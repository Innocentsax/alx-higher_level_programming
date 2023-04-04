#!/usr/bin/python3
def magic_string():
    my_magic_string = getattr(magic_string, 'n', 0) + 1
    return ("BestSchool, " * (my_magic_string - 1) + "BestSchool")
