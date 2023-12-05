#!/usr/bin/python3
"""Module for converting an object to its JSON representation"""

import json


def to_json_string(my_obj):
    """
    Convert an object to its JSON representation (string).

    Args:
        my_obj: The object to be converted.

    Returns:
        str: The JSON representation of the object.
    """
    return json.dumps(my_obj)
