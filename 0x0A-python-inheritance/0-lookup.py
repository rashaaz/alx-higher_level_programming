#!/usr/bin/python3
"""Module for look"""


def lookup(obj):
    """Returns a list containing the names of available attributes

    Args:
        obj: The object for which to retrieve attributes and methods.

    Returns:
        A list of strings representing the names of attributes and methods.
    """
    return dir(obj)
