#!/usr/bin/env python3
from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract class representing an Animal"""

    @abstractmethod
    def sound(self):
        """Abstract method to be implemented by subclasses"""
        pass


class Dog(Animal):
    """Subclass representing a Dog"""

    def sound(self):
        return "Bark"


class Cat(Animal):
    """Subclass representing a Cat"""

    def sound(self):
        return "Meow"
