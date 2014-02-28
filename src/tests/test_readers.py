# -*- coding: utf-8 -*-
"""
Created on 28/02/2014

@author: Frieder Czeschla
"""

import os
import trs.actors
import trs.readers
import unittest


class TestReaderFIn(unittest.TestCase):
    _robot = None

    def setUp(self):
        board = trs.actors.Board(5, 5)
        self._robot = trs.actors.Robot(board)

    def test_run_valid(self):
        file_path_abs = os.path.abspath(os.path.join((__file__),
                                                     "../../",
                                                     "commands.txt"))
        cmds_reader = trs.readers.CmdsReaderFIn(self._robot, file_path_abs)
        self.assertTrue(cmds_reader.run(verbose=False))

    def test_run_invalid(self):
        file_path_abs = os.path.abspath(os.path.join((__file__),
                                                     "../../",
                                                     "foo.bar"))
        cmds_reader = trs.readers.CmdsReaderFIn(self._robot, file_path_abs)
        self.assertFalse(cmds_reader.run(verbose=False))

if __name__ == "__main__":
    unittest.main()
