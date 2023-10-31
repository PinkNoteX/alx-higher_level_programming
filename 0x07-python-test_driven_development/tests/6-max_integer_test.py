#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """test for maxintegar """
    def test_max_f(self):
        alist = [9, 2, 3, 4]
        self.assertEqual(max_integer(alist), 9)
    
    def test_max_b(self):
        alist = [9, 2, 3, 99]
        self.assertEqual(max_integer(alist), 99)
    
    def test_max_m(self):
        alist = [9, 2 ,86, 33, 6]
        self.assertEqual(max_integer(alist), 86)
    
    def test_max_l(self):
        alist = [1, 2, 3, 4, 5, 77, 88, 99, 0, 56]
        self.assertEqual(max_integer(alist), 99)
    
    def test_negative(self):
        alist = [-22, -1, -3, -4]
        self.assertEqual(max_integer(alist), -1)
    
    def test_none(self):
        with self.assertRaises(TypeError):
            max_integer(None)
    
    def empty_list(self):
        self.assertEqual(max_integer([]), None)
    
    def isnone_test(self):
        alist = []
        self.assertEqual(max_integer(alist), None)
    
    def with_string(self):
        self.assertEqual(max_integer("string"), "t")
    
    def mixed_cases_test(self):
        alist = [2, 3, 4, 5, 'd']
        self.assertEqual(max_integer(alist), "d")

