#!/usr/bin/python3
def search_replace(my_list, search, replace):  # Define the prototype
    # Create a new list where each occurrence of 'search' is replaced
    return [replace if element == search else element for element in my_list]
