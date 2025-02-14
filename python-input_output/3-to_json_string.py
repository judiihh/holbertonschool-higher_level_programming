#!/usr/bin/python3
"""
This module contains the function `to_json_string`
which converts a Python object to a JSON string.
"""

import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string).

    Args:
        my_obj (any): The object to convert into a JSON string.

    Returns:
        str: The JSON representation of the object.
    """
    return json.dumps(my_obj)
