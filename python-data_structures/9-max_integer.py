#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:  # Check if the list is empty
        return None

    # Initialize the maximum value with the first element of the list
    max_val = my_list[0]

    # Iterate through the list to find the maximum value
    for num in my_list:
        if num > max_val:
            max_val = num

    return max_val
