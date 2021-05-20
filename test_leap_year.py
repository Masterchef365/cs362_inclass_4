#!/usr/bin/env python3
import unittest
from leap_year import is_leap_year

class LeapYearTest(unittest.TestCase):
    def test_is_leap_year(self):
        self.assertTrue(is_leap_year(2000))
        self.assertTrue(is_leap_year(2020))
        self.assertTrue(is_leap_year(1968))

        self.assertFalse(is_leap_year(2003))
        self.assertFalse(is_leap_year(2021))
        self.assertFalse(is_leap_year(1961))

    def test_type(self):
        with self.assertRaises(TypeError):
            is_leap_year(2.3)
        with self.assertRaises(TypeError):
            is_leap_year("wow")

    def test_negative(self):
        with self.assertRaises(ValueError):
            is_leap_year(-213)


if __name__ == '__main__':
    unittest.main()
