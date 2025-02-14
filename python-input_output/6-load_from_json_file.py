#!/usr/bin/python3
"""
This module contains the function `load_from_json_file`
which creates a Python object from a JSON file.
"""

import json


def load_from_json_file(filename):
    """
    Creates a Python object from a JSON file.

    Args:
        filename (str): The name of the file to read from.

    Returns:
        any: The Python object represented by the JSON file.
    """
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
