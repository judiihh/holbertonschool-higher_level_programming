#!/usr/bin/env python3

class Fish:
    """Represents a Fish with swimming ability"""

    def swim(self):
        print("The fish is swimming")

    def habitat(self):
        print("The fish lives in water")


class Bird:
    """Represents a Bird with flying ability"""

    def fly(self):
        print("The bird is flying")

    def habitat(self):
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """Represents a Flying Fish with both swimming and flying abilities"""

    def fly(self):
        print("The flying fish is soaring!")

    def swim(self):
        print("The flying fish is swimming!")

    def habitat(self):
        print("The flying fish lives both in water and the sky!")

# Testing Method Resolution Order (MRO)


if __name__ == "__main__":
    print(FlyingFish.mro())  # Print method resolution order
