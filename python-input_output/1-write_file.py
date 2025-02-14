#!/usr/bin/python3
"""
This module contains the function `write_file`
which writes a UTF-8 text file and returns the number of characters written.
"""


def write_file(filename="", text=""):
    """
    Writes a UTF-8 text file and returns the number of characters written.

    Args:
        filename (str): The name of the file to write to.
        text (str): The text to write in the file.

    Returns:
        int: The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
