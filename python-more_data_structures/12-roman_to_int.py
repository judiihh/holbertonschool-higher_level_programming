#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    # Mapping of Roman numerals to integers
    roman_map = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    # Initialize variables
    total = 0
    prev_value = 0

    # Traverse the string in reverse
    for char in reversed(roman_string):
        current_value = roman_map.get(char, 0)

        # Add or subtract based on Roman numeral rules
        if current_value < prev_value:
            total -= current_value
        else:
            total += current_value

        prev_value = current_value

    return total
