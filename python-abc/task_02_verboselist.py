#!/usr/bin/env python3

class VerboseList(list):
    """Custom list class that prints notifications when modified"""

    def append(self, item):
        """Overrides append method to print a notification"""
        super().append(item)
        print(f"Added {item} to the list.")

    def extend(self, iterable):
        """Overrides extend method to print a notification"""
        num_items = len(iterable)
        super().extend(iterable)
        print(f"Extended the list with {num_items} items.")

    def remove(self, item):
        """Overrides remove method to print a notification"""
        if item in self:
            print(f"Removed {item} from the list.")
            super().remove(item)
        else:
            print(f"Item {item} not found in the list.")

    def pop(self, index=-1):
        """Overrides pop method to print a notification"""
        if self:  # Check if the list is not empty
            item = super().pop(index)
            print(f"Popped {item} from the list.")
            return item
        else:
            print("Cannot pop from an empty list.")
            return None
