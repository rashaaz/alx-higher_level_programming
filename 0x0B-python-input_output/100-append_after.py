#!/usr/bin/python3
"""Function to insert a line of text to a file after each line"""


def append_after(filename="", search_string="", new_string=""):
    """
    Insert a line of text after each line containing a specific string.

    Args:
        filename (str): The name of the file.
        search_string (str): The string to search for in each line.
        new_string (str): The string to insert after each line.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        lines = []
        while True:
            li = file.readline()
            if li == "":
                break
            lines.append(li)
            if search_string in li:
                lines.append(new_string)
    with open(filename, 'w', encoding='utf-8') as file:
        file.writelines(lines)
