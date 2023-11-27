#!/usr/bin/python3
"""Define a Rectangle class"""


class Rectangle:
    """int: Rectangle class with private width and height attributes"""

    number_of_instances = 0
    """type: Initialized to 0. Incremented instance instantiationi"""

    print_symbol = "#"
    """Initialized to #. Used as a symbol for string representation"""

    def __init__(self, width=0, height=0):
        """Initialize the rectangle with optional width and height"""
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieve the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle, with error checking"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle, with error checking"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Compute the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Compute the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return a string representation of the rectangle"""
        if not self.__width or not self.__height:
            return ""
        return ((str(self.print_symbol) * self.__width + "\n") *
                self.__height)[:-1]

    def __repr__(self):
        """Return a string representation of the rectangle for reproduction"""
        return "Rectangle(" + str(self.__width)
        + ", " + str(self.__height) + ")"

    def __del__(self):
        """Print a message when an instance of Rectangle is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
