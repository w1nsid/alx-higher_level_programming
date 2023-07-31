#!/usr/bin/python3
"""Defines a foundational geometry class BaseGeometry."""


class BaseGeometry:
    """Denotes a basic geometric object."""

    def area(self):
        """Method yet to be implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that a parameter is a positive integer.

        Args:
            name (str): The name of the parameter.
            value (int): The parameter to validate.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
