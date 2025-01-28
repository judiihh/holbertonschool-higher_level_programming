#!/usr/bin/python3
"""

This module defines a class Square with size, position validation,
and methods to calculate area and print the square with coordinates.
"""


class Square:
    """

    A class that defines a square.
    """
    def __init__(self, size=0, position=(0, 0)):
        """

        Initializes a new square with a given size and position.

        Args:
            size (int): The size of the square (must be >= 0).
            position (tuple): The pos of the sq (must be a tuple of 2 + int)

        Raises:
            TypeError: If size or position are invalid.
            ValueError: If size is less than 0.
        """
        self.size = size  # Use the setter for validation
        self.position = position  # Use the setter for validation

    @property
    def size(self):
        """

        Getter for the size attribute.

        Returns:
            int: The size of the square.
        Also provides controlled access to the private attribute __size, and
        Allows you to retrieve the value from outside the class
        """
        return self.__size

    @size.setter  # Validates the new value assigned to size
    def size(self, value):
        """

        Setter for the size attribute.

        Args:
            value (int): The new size of the square (must be >= 0).

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):  # Ensures the size parameter is an int
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value  # Private instance attribute

    @property
    def position(self):
        """
        Getter for the position attribute.

        Returns:
            tuple: The position of the square.
         """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter for the position attribute.

        Args:
            value (tuple): The new pos of the sq (must be a tuple of 2+ int).

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(i, int) for i in value) or
                not all(i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """

        Calculates and returns the area of the square.

        Returns:
            int: The area of the square (size * size).
        """
        return self.__size * self.__size  # __size stores the square's size
        # Formula this public method calculates the area of the sq

    def my_print(self):
        """

        Prints the square with the character '#' to stdout,
        using spaces to respect the position attribute.

        If size is 0, prints an empty line.
        """
        if self.__size == 0:
            print("")
            return

        print("\n" * self.__position[1], end="")
        # Print new lines for vertical offset

        # Print the square with horizontal offset
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
