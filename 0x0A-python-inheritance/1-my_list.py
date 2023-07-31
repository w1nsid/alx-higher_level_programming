#!/usr/bin/python3
"""Defines a subclass of the built-in list class named MyList."""


class MyList(list):
    """Provides a method for printing the list in a sorted manner."""

    def print_sorted_list(self):
        """Print the list items in sorted ascending order."""
        print(sorted(self))
