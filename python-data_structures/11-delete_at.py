#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        return my_list  # Return the original list if idx is invalid
    del my_list[idx]  # Use `del` to remove the item at the specified index
    return my_list
