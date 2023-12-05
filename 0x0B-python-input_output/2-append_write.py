#!/usr/bin/python3
"""Module for appending a string to the end of a text file (UTF8)."""


def append_write(filename="", text=""):
    """
    Append a string to the end of a text file (UTF8) and return number

    Args:
        filename (str): The name of the file to append.
        text (str): The string to be appended to the file.

    Returns:
        int: The number of characters added.
    """
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)
