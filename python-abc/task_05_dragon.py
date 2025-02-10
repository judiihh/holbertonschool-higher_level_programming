#!/usr/bin/env python3

class SwimMixin:
    """Mixin that provides swimming ability"""

    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """Mixin that provides flying ability"""

    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Dragon class that can both swim and fly"""

    def roar(self):
        print("The dragon roars!")
