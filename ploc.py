#!/usr/bin/env python

import sys
import os

class PythonFile(object):
    def __init__(self, path):
        if not os.path.isfile(path):
            raise Exception("'%s' is not a valid file" % path)

        if not path.endswith('.py'):
            raise Exception("'%s' is not a python file" % path)

        with open(path) as file:
            self.lines = file.readlines()

    def significant_lines(self):
        # List of lines with insignificant characters removed
        significant_char_lines = [PythonFile.strip_insignificant(line) for line in self.lines]

        # Debugging
        #print("Significant char lines", significant_char_lines)

        # List of lines that have significant characters
        return [line for line in significant_char_lines if len(line) > 0]


    @staticmethod
    def strip_insignificant(line):
        """Strip insignificant characters from a line of Python.

        Insignificant characters in python are:
            * Characters participating in comments
            * Trailing whitespace

        IMPORTANT: Ensure that trailing whitespace is removed AFTER comments,
                   otherwise we could be left with whitespace before the comment"""
        return PythonFile.strip_trailing_whitespace(PythonFile.strip_comments(line))


    @staticmethod
    def strip_comments(line):
        """Strip comments from a line of Python.

        Python comments are prefixed with a '#' symbol"""
        return line.split('#')[0]


    @staticmethod
    def strip_trailing_whitespace(line):
        """Strip trailing whitespace from a line of Python.

        Leading whitespace is significant in Python, so make sure to only strip
        trailing whitespace."""
        return line.rstrip()


if __name__ == '__main__':
    file = PythonFile(sys.argv[1])

    print(len(file.significant_lines()))
