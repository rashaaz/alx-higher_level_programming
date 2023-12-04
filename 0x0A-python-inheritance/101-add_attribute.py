#!/usr/bin/python3
"""Module 101-add_attribute Defines a function that adds a new attribute"""


def add_attribute(obj, attr_name, attr_value):
    """Adds a new attribute to an object if it's possible."""
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, attr_name, attr_value)
