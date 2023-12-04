#!/usr/bin/python3
"""Module 100-my_int Defines a MyInt class"""


class MyInt(int):
    """A class representing a rebel integer."""

    def __new__(cls, *args, **kwargs):
        """Inverts the new instance operator."""
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, other):
        """Inverts the equality operator."""
        return int(self) != other

    def __ne__(self, other):
        """Inverts the inequality operator."""
        return int(self) == other
