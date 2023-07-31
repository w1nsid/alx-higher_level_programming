#!/usr/bin/python3
"""Defines a function to check class type."""


def is_same_class(obj, a_class):
    """Determine if an object is exactly an instance of a specific class.

    Args:
        obj (any): The object to examine.
        a_class (type): The class to compare with the type of obj.
    Returns:
        True if obj is exactly an instance of a_class, otherwise False.
    """
    if type(obj) == a_class:
        return True
    return False
