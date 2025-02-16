#!/usr/bin/python3
"""
This module defines the function `pascal_triangle`
which generates Pascal's Triangle of a given size.
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing Pascal’s triangle of n.

    Args:
        n (int): The number of rows in Pascal's triangle.

    Returns:
        list: A list of lists representing Pascal’s triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]  # First row is always [1]

    for i in range(1, n):
        prev_row = triangle[-1]  # Last row in the triangle
        new_row = [1]  # Every row starts with 1

        # Generate the middle values of the row
        for j in range(1, len(prev_row)):
            new_row.append(prev_row[j - 1] + prev_row[j])

        new_row.append(1)  # Every row ends with 1
        triangle.append(new_row)

    return triangle
