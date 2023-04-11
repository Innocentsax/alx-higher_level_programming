#!/usr/bin/python3
"""Defines an subclass or child list class MyList."""


class MyList(list):
    """These class is a subclass of the list class."""

    def print_sorted(self):
        """Print a sorted list in a specific pattern."""
        print(sorted(self))
