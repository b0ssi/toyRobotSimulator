#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on 28/02/2014

@author: Frieder Czeschla

Runs all of the project's tests.
"""

import tests.test_actors
import tests.test_readers
import unittest

if __name__ == "__main__":
    suite = unittest.TestSuite()
    loader = unittest.defaultTestLoader
    for loaded_tests in [loader.loadTestsFromTestCase(tests.test_actors.TestRobot),
                         loader.loadTestsFromTestCase(tests.test_readers.TestCmdsReaderFIn)]:
        suite.addTests(loaded_tests)
    unittest.TextTestRunner().run(suite)
