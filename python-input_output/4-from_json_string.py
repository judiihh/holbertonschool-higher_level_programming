#!/usr/bin/python3
"""
This module contains the function `from_json_string`
which converts a JSON string into a Python object.
"""

import json


def from_json_string(my_str):
    """
    Returns the Python object represented by a JSON string.

    Args:
        my_str (str): The JSON string to convert.

    Returns:
        any: The corresponding Python object.
    """
    return json.loads(my_str)
