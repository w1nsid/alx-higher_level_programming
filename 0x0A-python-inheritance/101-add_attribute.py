#!/usr/bin/python3
"""Defines a function that appends attributes to objects."""


def add_attribute(obj, att, value):
    """Assigns a new attribute to an object if feasible.

    Args:
        obj (any): The object to append an attribute to.
        att (str): The name of the attribute to add to obj.
        value (any): The value of att.
    Raises:
        TypeError: If the attribute cannot be appended.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
