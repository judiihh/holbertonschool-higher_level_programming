#!/usr/bin/python3
"""
This module provides a function
to print text with 2 new lines after: '.', '?', and ':'.
"""


def text_indentation(text):
    """
    Prints text with 2 new lines after chars: '.', '?', and ':'.

    Args:
        text (str): The text to be processed.

    Raises:
        TypeError: If text is not a string.
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    i = 0
    while i < len(text):
        if text[i] in ['.', '?', ':']:
            print(text[i])
            print()
            if i + 1 < len(text) and text[i + 1] == " ":
                while i + 1 < len(text) and text[i + 1] == " ":
                    i += 1
        else:
            print(text[i], end="")
        i += 1
