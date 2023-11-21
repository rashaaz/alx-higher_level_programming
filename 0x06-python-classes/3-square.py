"""the Square class."""


class Square:
    """The defines for the Square class"""

    def __init__(self, size=0):
        """This is the constructor.

        Args:
            size: The square size.
            TypeError: if it not integer
            ValueError: size is not be >= 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """method calculate the area of the square.

        Returns:
            The area of the square.
        """
        return self.__size ** 2
