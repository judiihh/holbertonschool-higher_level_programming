#!/usr/bin/python3
"""
This module contains the function `read_file`
which reads a UTF-8 text file and prints its content.
"""


def read_file(filename=""):
    """
    Reads a UTF-8 text file and prints its content to stdout.

    Args:
        filename (str): The name of the file to read.
    """
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read(), end="")
