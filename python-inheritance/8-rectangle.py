#!/usr/bin/python3
"""
Module containing the Rectangle class, inheriting from BaseGeometry.
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class that inherits from BaseGeometry."""

    def __init__(self, width, height):
        """
        Initializes a rectangle with width and height.

        Args:
            width (int): The width of the rectangle (must be a + int).
            height (int): The height of the rectangle (must be a + int).
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
