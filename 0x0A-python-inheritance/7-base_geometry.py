#!/usr/bin/python3
"""Defines a foundational geometry class BaseGeometry."""


class BaseGeometry:
    """Denotes a basic geometric object."""

    def area(self):
        """Method yet to be implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, parameter_name, parameter_value):
        """Validates that a parameter is a positive integer.

        Args:
            parameter_name (str): The name of the parameter.
            parameter_value (int): The parameter to validate.
        Raises:
            TypeError: If parameter_value is not an integer.
            ValueError: If parameter_value is <= 0.
        """
        if type(parameter_value) != int:
            raise TypeError("{} must be an integer".format(parameter_name))
        if parameter_value <= 0:
            raise ValueError(
                "{} must be greater than 0".format(parameter_name)
            )
