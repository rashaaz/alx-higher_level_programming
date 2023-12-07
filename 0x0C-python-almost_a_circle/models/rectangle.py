#!/usr/bin/python3
"""Module for importing the Base class from models.base"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class that inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize Rectangle instance"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter method for the width attribute."""
        return self.__width

    @width.setter
    def width(self, value):
        self.val_nt("width", value, False)
        self.__width = value

    @property
    def height(self):
        """Getter method for the height attribute."""
        return self.__height

    @height.setter
    def height(self, value):
        self.val_nt("height", value, False)
        self.__height = value

    @property
    def x(self):
        """Getter method for the x attribute."""
        return self.__x

    @x.setter
    def x(self, value):
        self.val_nt("x", value)
        self.__x = value

    @property
    def y(self):
        """Getter method for the y attribute."""
        return self.__y

    @y.setter
    def y(self, value):
        self.val_nt("y", value)
        self.__y = value

    def val_nt(self, n, value, equle=True):
        """Validate if a value is an integer greater than 0"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(n))
        if equle and value < 0:
            raise ValueError("{} must be >= 0".format(n))
        elif not equle and value <= 0:
            raise ValueError("{} must be > 0".format(n))

    def area(self):
        """Calculate the area of the rectangle"""
        return self.width * self.height

    def display(self):
        """Display the rectangle on the standard output"""
        r = '\n' * self.y + \
            (' ' * self.x + '#' * self.width + '\n') * self.height
        print(r, end='')

    def __str__(self):
        """String representation of the Rectangle object."""
        return '[{}] ({}) {}/{} - {}/{}'.\
            format(type(self).__name__, self.id, self.x, self.y, self.width,
                   self.height)

    def __update(self, id=None, width=None, height=None, x=None, y=None):
        """Update attributes of the Rectangle object"""
        if id is not None:
            self.id = id
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        """Update attributes using arguments or keywords."""
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)

    def to_dictionary(self):
        """Convert the Rectangle object to a dictionary"""
        return {"id": self.id, "width": self.__width, "height": self.__height,
                "x": self.__x, "y": self.__y}
