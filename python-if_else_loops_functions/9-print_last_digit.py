#!/usr/bin/python3
def print_last_digit(number):
    """Prints and returns the last digit of a number."""
    last_digit = abs(number) % 10  # Get the absolute value of the last digit
    print("{}".format(last_digit), end="")
    # Print the last digit without a newline
    return last_digit
