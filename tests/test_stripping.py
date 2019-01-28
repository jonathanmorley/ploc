#!/usr/bin/env python

import unittest
from ploc import PythonFile


class TestStripping(unittest.TestCase):

    def test_strip_trailing_whitespace(self):
        self.assertEqual(PythonFile.strip_trailing_whitespace("foo"), "foo")
        self.assertEqual(PythonFile.strip_trailing_whitespace("foo   "), "foo")
        self.assertEqual(PythonFile.strip_trailing_whitespace("   foo   "), "   foo")


    def test_strip_comments(self):
        self.assertEqual(PythonFile.strip_comments("foo  "), "foo  ")
        self.assertEqual(PythonFile.strip_comments("foo  # bar"), "foo  ")
        self.assertEqual(PythonFile.strip_comments("# bar"), "")


    def test_strip_insignificant(self):
        self.assertEqual(PythonFile.strip_insignificant("   foo  # bar"), "   foo")
        self.assertEqual(PythonFile.strip_insignificant("foo  # bar"), "foo")

if __name__ == '__main__':
    unittest.main()
