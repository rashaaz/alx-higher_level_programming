#!/usr/bin/python3
"""Module for saving an object to a JSON file"""

import json


def save_to_json_file(my_obj, filename):
    """
    Save an object to a JSON file.

    Args:
        my_obj: The object to be saved.
        filename (str): The name of the file to save the object to.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)
