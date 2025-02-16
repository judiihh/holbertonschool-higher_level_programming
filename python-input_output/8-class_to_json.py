#!/usr/bin/python3
"""
This module contains the function `class_to_json`
which returns the dictionary description of an object
for JSON serialization.
"""


def class_to_json(obj):
    """
    Returns the dictionary representation of an object.

    Args:
        obj (any): An instance of a class.

    Returns:
        dict: A dictionary containing all serializable attributes.
    """
    return obj.__dict__
