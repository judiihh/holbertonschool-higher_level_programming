#!/usr/bin/python3
"""
This module provides a function to add two integers or floats.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats and returns the result as an integer.

    Args:
        a (int, float): The first number to add.
        b (int, float): The second number to add. Defaults to 98.

    Returns:
        int: The sum of the two numbers as an integer.

    Raises:
        TypeError: If either a or b is not an integer or float.
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    if (a + b) == float('inf') or (a + b) == -float('inf'):
        raise OverflowError("Cannot convert float infinity to int")
    return int(a) + int(b)
