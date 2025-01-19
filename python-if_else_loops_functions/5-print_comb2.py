#!/usr/bin/python3
for i in range(100):
    if i == 99:
        print("{:02d}".format(i))  # Print the last number without a comma
    else:
        print("{:02d}, ".format(i), end="")
        # Print with a comma and no newline
