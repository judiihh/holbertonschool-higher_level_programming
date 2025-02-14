#!/usr/bin/python3
"""
This module contains the function `append_write`
which appends text to a UTF-8 txt file and returns the # of chars added.
"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a UTF-8 txt file
    and returns the # of chars added.

    Args:
        filename (str): The name of the file to append to.
        text (str): The text to append.

    Returns:
        int: The number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
