#!/usr/bin/env python3
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract class representing a Shape"""

    @abstractmethod
    def area(self):
        """Abstract method for calculating area"""
        pass

    @abstractmethod
    def perimeter(self):
        """Abstract method for calculating perimeter"""
        pass


class Circle(Shape):
    """Circle shape with a radius"""

    def __init__(self, radius):
        self.radius = abs(radius)  # Convert - radius to +

    def area(self):
        """Calculate and return the area of the circle"""
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Calculate and return the perimeter (circumference) of the circle"""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle shape with width and height"""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """Calculate and return the area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Calculate and return the perimeter of the rectangle"""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Print the area and perimeter of a shape using duck typing"""
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
