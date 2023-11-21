#!/usr/bin/python3
"""Define  MagicClass."""

import math


class MagicClass:
    """Represent a magic class."""

    def __init__(self, radius=0):
        """Initialize a new MagicClass.

        Args:
            radius (int or float):  radius of  circle.
        """
        if type(radius) not in [int, float]:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """the area of the circle."""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """circumference of the circle."""
        return 2 * math.pi * self.__radius
