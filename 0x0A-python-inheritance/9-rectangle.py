#!/usr/bin/python3
"""Defines a Rectangle class that inherits from BaseGeometry."""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Defines a rectangle using BaseGeometry."""

    def __init__(self, width, height):
        """Constructs a new Rectangle instance.

        Args:
            width (int): The width of the Rectangle.
            height (int): The height of the Rectangle.
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Computes the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Generates a string representation of the Rectangle."""
        rectangle_representation = "[" + str(self.__class__.__name__) + "] "
        rectangle_representation += (
            str(self.__width) + "/" + str(self.__height)
        )
        return rectangle_representation
