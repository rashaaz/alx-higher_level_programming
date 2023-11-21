#!/usr/bin/python3
"""the Square class."""


class Square:
    """The defines for the Square class"""

    def __init__(self, size=0):
        """This is the constructor.

        Args:
            size: The square size.
        """
        self.size = size

    @property
    def size(self):
        """Property retrieve the size of the square.

        Raises:
            TypeError: if it not integer
            ValueError: size is not be >= 0
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """method calculate the area of the square.

        Returns:
            The area of the square.
        """
        return self.__size ** 2

    def __eq__(self, other):
        return self.area() == other.area()

    def __ne__(self, other):
        return self.area() != other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __le__(self, other):
        return self.area() <= other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __ge__(self, other):
        return self.area() >= other.area()
