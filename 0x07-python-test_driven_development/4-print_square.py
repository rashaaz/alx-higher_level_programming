#!/usr/bin/python3
"""Module to print a square of a specified size."""


def print_square(size):
    """Print a square made of '#' characters with the specified size.

    Args:
        size (int): The size of the square.

    Raises:
        TypeError: If the provided size is not an integer.
        ValueError: If the provided size is less than 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    print((("#" * size + "\n") * size), end="")

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
