#!/usr/bin/python3
"""This script describes a function for computing the sum of two integers."""


def sum_integers(param1, param2=98):
    """Returns the result of the addition operation for two numbers.

    In case of float type arguments, they are converted to integers before
    the addition operation is performed.

    Raises:
        TypeError: If either of param1 or param2 is not an integer or a float.
    """
    if ((not isinstance(param1, int) and not isinstance(param1, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(param2, int) and not isinstance(param2, float))):
        raise TypeError("b must be an integer")
    return (int(param1) + int(param2))
