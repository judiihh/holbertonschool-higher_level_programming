#!/usr/bin/python3
"""

This module defines a class Square with a private instance attribute.
"""


class Square:
    """

    A class that defines a square.
    """
    def __init__(self, size):
        """

        Initializes a new square with a given size.

        Args:
            size (int): The size of the square (private).
        """
        self.__size = size  # Private instance attribute
