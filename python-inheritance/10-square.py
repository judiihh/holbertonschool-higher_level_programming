#!/usr/bin/python3
"""
Module containing the Square class, inheriting from Rectangle.
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle."""

    def __init__(self, size):
        """
        Initializes a square with size.

        Args:
            size (int): The size of the square (must be a + int).
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
