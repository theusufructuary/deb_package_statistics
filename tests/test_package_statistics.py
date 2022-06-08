#!/bin/python3

import unittest

from http.client import HTTPResponse

import package_statistics


class TestPackageStatistics(unittest.TestCase):

    def test_get_contents_file(self):
        self.assertEqual(HTTPResponse, type(package_statistics.contents))
    # Test logging

    def test_format_lines(self):
        self.assertEqual(dict, type(package_statistics.counter))
        self.assertNotEqual(0, package_statistics.counter.values)
    # Test for '/' in package names


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
