#!/usr/bin/python3
"""

This module defines a class Square with size validation, a getter and setter,
and an area method.
"""


class Square:
    """

    A class that defines a square.
    """
    def __init__(self, size=0):  # init method assigns size using the setter
        """

        Initializes a new square with a given size.

        Args:
            size (int): The size of the square (must be >= 0).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.size = size  # Use the setter for validation

    @property
    def size(self):
        """

        Getter for the size attribute.

        Returns:
            int: The size of the square.
        Also provides controlled access to the private attribute __size, and
        Allows you to retrieve the value from outside the class
        """
        return self.__size

    @size.setter  # Validates the new value assigned to size
    def size(self, value):
        """

        Setter for the size attribute.

        Args:
            value (int): The new size of the square (must be >= 0).

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):  # Ensures the size parameter is an int
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value  # Private instance attribute

    def area(self):
        """

        Calculates and returns the area of the square.

        Returns:
            int: The area of the square (size * size).
        """
        return self.__size * self.__size  # __size stores the square's size
        # Formula this public method calculates the area of the sq
