#!/usr/bin/python3
"""Define a function inherits_from"""


def inherits_from(obj, a_class):
    """Check if an object is an instance of a class"""
    return isinstance(obj, a_class) and type(obj) != a_class
