#!/usr/bin/env python3

class CountedIterator:
    """Iterator wrapper that counts the number of items iterated over"""

    def __init__(self, iterable):
        """Initialize with an iterable and set up a counter"""
        self.iterator = iter(iterable)
        self.count = 0

    def __iter__(self):
        """Returns itself as an iterator"""
        return self

    def __next__(self):
        """Fetch the next item and increment the count"""
        try:
            item = next(self.iterator)
            self.count += 1
            return item
        except StopIteration:
            raise StopIteration

    def get_count(self):
        """Returns the number of items retrieved so far"""
        return self.count
