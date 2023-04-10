#!/usr/bin/python3
"""
Unittest for max_integer([..])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ test class """
    def setUp(self):
        """ setup variables """
        self.list1 = [1, 3, 23, 54]
        self.list2 = [2.23, 3.43, 0, 0.43]
        self.list3 = []  # return None for empty list
        self.list4 = [6]
        self.list5 = [6, 3.4, 10, 32.5]
        self.list6 = [10, 2, 4, 5, 6]  # max at beginning
        self.list7 = [2, 4, 5, -4, 3]  # 1 negative num
        self.list8 = [-2, -4, -1, -5, -6]

    def test_integers_list(self):
        """ test for max_integer int int list"""
        ans = max_integer(self.list1)
        self.assertEqual(ans, 54)

    def test_floats_list(self):
        """ test list with floats only"""
        ans = max_integer(self.list2)
        self.assertEqual(ans, 3.43)

    def test_empty_list(self):
        """ test empty list"""
        ans = max_integer(self.list3)
        self.assertEqual(ans, None)

    def test_single_element(self):
        """ test list with one element"""
        ans = max_integer(self.list4)
        self.assertEqual(ans, 6)

    def test_floats_ints(self):
        """ test list with floats and ints"""
        ans = max_integer(self.list5)
        self.assertEqual(ans, 32.5)

    def test_max_beg(self):
        """ test max number at beginning """
        ans = max_integer(self.list6)
        self.assertEqual(ans, 10)

    def test_neg_element(self):
        """ test case: one negative element """
        ans = max_integer(self.list7)
        self.assertEqual(ans, 5)

    def test_all_negative(self):
        """ test case: all elements are negative"""
        ans = max_integer(self.list8)
        self.assertEqual(ans, -1)


if __name__ == "__main__":
    unittest.main()
