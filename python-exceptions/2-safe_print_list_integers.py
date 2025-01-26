#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            # Skip non-integer values
            continue
        except IndexError:
            # Stop iterating if the list is shorter than x
            break
    print()  # Print a new line at the end
    return count
