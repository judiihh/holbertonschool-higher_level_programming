#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    # Check if the key exists in the dictionary and delete it
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
