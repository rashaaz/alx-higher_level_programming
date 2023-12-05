#!/usr/bin/python3
"""Function that returns the dictionary"""


def class_to_json(obj):
    """Converts an instance of a class to a dictionary"""
    return obj.__dict__
