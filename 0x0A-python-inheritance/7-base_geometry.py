#!/usr/bin/python3
"""Define a class BaseGeometry."""


class BaseGeometry:
    """A class representing BaseGeometry."""

    def area(self):
        """Raise an Exception with the message 'area() is not implemented'."""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate the value."""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
