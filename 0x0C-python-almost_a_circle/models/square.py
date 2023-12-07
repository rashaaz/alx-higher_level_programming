#!/usr/bin/python3
"""Module for inherits from rectangle class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class, inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize Square instance."""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return the string representation of the Square."""
        return '[{}] ({}) {}/{} - {}'.\
            format(type(self).__name__, self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """Get the size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __up_me(self, id=None, size=None, x=None, y=None):
        """Update the Square attributes."""
        if id is not None:
            self.id = id
        if size is not None:
            self.size = size
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        """Update Square attributes using arguments or keyword"""
        if args:
            self.__up_me(*args)
        elif kwargs:
            self.__up_me(**kwargs)

    def to_dictionary(self):
        """Return the dictionary representation of the Square."""
        return {"id": self.id, "size": self.width,
                "x": self.x, "y": self.y}
