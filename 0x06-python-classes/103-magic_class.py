#!/usr/bin/python3
"""Define a class MagicClass."""

import math


class MagicClass:
    """Represent a magic class."""

    def __init__(self, radius=0):
        """Initialize a new MagicClass.

        Args:
            radius (int or float): The radius of the circle.
        """
        if type(radius) not in [int, float]:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Calculate the area of the circle."""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Calculate the circumference of the circle."""
        return 2 * math.pi * self.__radius
