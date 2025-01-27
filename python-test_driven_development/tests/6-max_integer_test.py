#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max_at_end(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_at_beginning(self):
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_max_in_middle(self):
        self.assertEqual(max_integer([1, 4, 3, 2]), 4)

    def test_one_element(self):
        self.assertEqual(max_integer([4]), 4)

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([-1, 2, -3, 4]), 4)

    def test_all_same_numbers(self):
        self.assertEqual(max_integer([4, 4, 4, 4]), 4)

    def test_list_with_floats(self):
        self.assertEqual(max_integer([1.1, 2.2, 3.3, 4.4]), 4.4)

    def test_list_with_ints_and_floats(self):
        self.assertEqual(max_integer([1, 2.2, 3, 4.4]), 4.4)

    def test_string(self):
        self.assertEqual(max_integer("holberton"), 't')

    def test_list_of_strings(self):
        self.assertEqual(max_integer(["abc", "def", "ghi"]), "ghi")

    def test_empty_string(self):
        self.assertEqual(max_integer(""), None)

if __name__ == '__main__':
    unittest.main()
