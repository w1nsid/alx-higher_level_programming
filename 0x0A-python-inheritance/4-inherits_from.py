#!/usr/bin/python3
"""Defines a function to check class inheritance."""


def inherits_from(obj, a_class):
    """Determines if an object is a subclass instance of a specified class.

    Args:
        obj (any): The object to verify.
        a_class (type): The class to match against the type of obj.
    Returns:
        True if obj is an inherited instance of a_class, otherwise False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
