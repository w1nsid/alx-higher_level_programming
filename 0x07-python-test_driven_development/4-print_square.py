#!/usr/bin/python3
"""This module contains a function to render a square using the # symbol."""


def print_square(dimension):
    """Display a square shape using the # character.

    Args:
        dimension (int): The height/width of the square to be printed.
    Raises:
        TypeError: If dimension is not an integer.
        ValueError: If dimension is < 0
    """
    if not isinstance(dimension, int):
        raise TypeError("size must be an integer")
    if dimension < 0:
        raise ValueError("size must be >= 0")

    for idx in range(dimension):
        [print("#", end="") for jdx in range(dimension)]
        print("")
