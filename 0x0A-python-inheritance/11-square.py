#!/usr/bin/python3
"""Module 11-square Defines a Square class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class representing a square."""
    def __init__(self, size):
        """
        Initializes a Square instance.
        Args:
            size (int): The size of the square.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        Computes the area of the rectangle.
        Returns:
            int: The area of the rectangle.
        """
        return self.__size ** 2

    def __str__(self):
        """
        Returns a string representation of the Square.
        """
        return "[Square] " + str(self.__size) + "/" + str(self.__size)
