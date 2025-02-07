#!/usr/bin/python3
"""
Module containing the is_kind_of_class function.
"""


def is_kind_of_class(obj, a_class):
    """Returns True if obj is an instance of a_class or a subclass of it,
    otherwise False.
    """
    return isinstance(obj, a_class)
