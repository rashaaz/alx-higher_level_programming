#!/usr/bin/python3
"""Module for MyList"""


class MyList(list):
    """MyList class inherits from the built-in list class"""
    def print_sorted(self):
        """Prints the list in ascending order."""
        print(sorted(self))
