#!/usr/bin/python3
"""Module to perform integer addition"""


def add_integer(a, b=98):
    """Add two integers or floats.

    Args:
        a (int or float): First number.
        b (int or float): Second number. Defaults to 98.

    Returns:
        int: Sum of the two numbers after converting them to integers.

    Raises:
        TypeError: If a or b is not an integer or float.
    """

    if type(a) not in (int, float):
        raise TypeError('a must be an integer')
    if type(b) not in (int, float):
        raise TypeError('b must be an integer')
    return int(a) + int(b)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
