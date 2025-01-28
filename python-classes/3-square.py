#!/usr/bin/python3
"""

This module defines a class Square with size validation and an area method.
"""


class Square:
    """

    A class that defines a square.
    """
    def __init__(self, size=0):  # Ainit method ensures size is an int and >=0
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

    def area(self):
        """

        Calculates and returns the area of the square.

        Returns:
            int: The area of the square (size * size).
        """
        return self.__size * self.__size  # __size stores the square's size
        # Formula this public method calculates the area of the sq
