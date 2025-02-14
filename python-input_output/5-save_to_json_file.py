#!/usr/bin/python3
"""
This module contains the function `save_to_json_file`
which writes an object to a file using JSON format.
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using a JSON representation.

    Args:
        my_obj (any): The object to serialize and save.
        filename (str): The name of the file to write to.
    """
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)
