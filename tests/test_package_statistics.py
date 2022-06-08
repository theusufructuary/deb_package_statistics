#!/bin/python3

import unittest

from regex import Regex

import package_statistics


class TestPackageStatistics(unittest.TestCase):

    def test_get_contents_file(self):
        self.assertTrue(Regex("<class 'http.client.HTTPResponse'>"), type(package_statistics.contents))
    # Test logging

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
