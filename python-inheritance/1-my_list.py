#!/usr/bin/python3
"""
Module containing the MyList class.
"""


class MyList(list):
    """Custom list class that inherits from list."""

    def print_sorted(self):
        """Prints the list in ascending sorted order."""
        print(sorted(self))  # sorted() returns a new sorted list
