#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            # Try to print the integer at index i
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            # Skip non-integer values silently
            continue
        except IndexError:
            # Stop iteration if x exceeds the list length
            break
    print()  # Print a single newline after the loop
    return count
