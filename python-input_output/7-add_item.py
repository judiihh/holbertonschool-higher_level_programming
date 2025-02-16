#!/usr/bin/python3
"""
This script adds all command-line arguments to a Python list
and saves them to the file `add_item.json`.
"""

import sys
import os
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

filename = "add_item.json"

# Step 1: Load existing data if the file exists,
# otherwise start with an empty list
if os.path.exists(filename):
    items = load_from_json_file(filename)
else:
    items = []

# Step 2: Add command-line arguments to the list
items.extend(sys.argv[1:])  # Append new arguments

# Step 3: Save the updated list back to the file
save_to_json_file(items, filename)
