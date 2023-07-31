#!/usr/bin/python3
"""Defines a function to check class inheritance."""


def is_kind_of_class(obj, a_class):
    """Check if an object is an instance or a derivative instance of a class.

    Args:
        obj (any): The object to examine.
        a_class (type): The class to compare with the type of obj.
    Returns:
        True if obj is an instance or derived instance of a_class, otherwise
        False.
    """
    if isinstance(obj, a_class):
        return True
    return False
