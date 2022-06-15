#!/bin/python3

import unittest

from modules import package_statistics

from http.client import HTTPResponse


class TestPackageStatistics(unittest.TestCase):

    def test_get_contents_file(self):
        self.assertEqual(HTTPResponse, type(package_statistics.contents))
        # To add in: test logging to syslog works as expected.
        # Also test that every file on Debian mirror downloads and
        # displays to terminal correctly

    def test_format_lines(self):
        self.assertEqual(dict, type(package_statistics.counter))
        self.assertNotEqual(0, package_statistics.counter.values)
        # To add in: test for '/' in package names

    # def test_sort_list(self):
        # To add in: test that key is string, and value is int
        # and only 10 lines are printed to the terminal
        # and that the sorting works as expected


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
