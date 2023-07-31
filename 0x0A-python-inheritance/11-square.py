#!/usr/bin/python3
"""Defines a Square class which is a subclass of Rectangle."""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Defines a square shape."""

    def __init__(self, size):
        """Constructs a new Square instance.

        Args:
            size (int): The size (length of a side) of the new square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
