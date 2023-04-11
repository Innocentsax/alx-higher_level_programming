#!/usr/bin/python3
"""Defines a class and inherited class-checking function."""


def is_kind_of_class(obj, a_class):
    """returns true if object is an instance of a class
    or a class that the class in question inherits from"""
    if isinstance(obj, a_class):
        return True
    return False
