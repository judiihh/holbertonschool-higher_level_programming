#!/usr/bin/python3
"""

This module defines a class Square with size validation.
"""


class Square:
    """

    A class that defines a square.
    """
    def __init__(self, size=0):  # Allows size to be optional
        """

        Initializes a new square with a given size.

        Args:
            size (int): The size of the square (must be >= 0).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):  # Ensures the size parameter is an int
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size  # Private instance attribute
