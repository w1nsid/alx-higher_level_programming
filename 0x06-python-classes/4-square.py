#!/usr/bin/python3

"""This module defines a class Square."""


class Square:
    """Represents an empty square."""

    def __init__(self, size=0):
        """Initialize a new Square.
        """
        self.size = size

    @property
    def size(self):
        """Get/set the current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Compute the area of this square."""
        return (self.__size * self.__size)
