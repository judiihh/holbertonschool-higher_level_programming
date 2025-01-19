#!/usr/bin/python3
def uppercase(str):
    """Prints a string in uppercase."""
    for char in str:
        if ord('a') <= ord(char) <= ord('z'):
            # Convert lowercase letter to uppercase by subtracting 32
            char = chr(ord(char) - 32)
        print("{}".format(char), end="")
    print()  # Print a newline at the end
