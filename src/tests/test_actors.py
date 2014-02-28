'''
Created on 28/02/2014

@author: Frieder Czeschla
'''

import unittest
import trs.actors


class TestRobot(unittest.TestCase):
    _robot = None
    _board_width = 5
    _board_height = 5

    def setUp(self):
        board = trs.actors.Board(self._board_width, self._board_height)
        self._robot = trs.actors.Robot(board)

    def test_place_pos_out_of_range(self):
        self.assertFalse(self._robot.place(-1, 0, "NORTH"))
        self.assertFalse(self._robot.place(self._board_width, 0, "NORTH"))
        self.assertFalse(self._robot.place(self._board_width, -1, "NORTH"))
        self.assertFalse(self._robot.place(self._board_width,
                                           self._board_height + 1,
                                           "NORTH"))

    def test_place_pos_in_range(self):
        for x in range(self._board_width):
            for y in range(self._board_height):
                self.assertTrue(self._robot.place(x, y, "NORTH"))

    def test_place_invalid_facing_dir(self):
        for f in ("north", "south", "east", "west", "foo", "bar"):
            self.assertFalse(self._robot.place(0, 0, f))

    def test_place_valid_facing_dir(self):
        for f in ("NORTH", "SOUTH", "EAST", "WEST"):
            self.assertTrue(self._robot.place(0, 0, f))

    def test_move_invalid(self):
        self._robot.place(0, 0, "NORTH")

        self.assertTrue(self._robot.move())
        self.assertTrue(self._robot.move())
        self.assertTrue(self._robot.move())
        self.assertTrue(self._robot.move())
        self.assertFalse(self._robot.move())

    def test_move_valid(self):
        self._robot.place(0, 0, "NORTH")

        self.assertTrue(self._robot.move())
        self.assertTrue(self._robot.move())
        self.assertTrue(self._robot.move())
        self.assertTrue(self._robot.move())

    def test_navigate_before_place(self):
        self.assertFalse(self._robot.move())
        self.assertFalse(self._robot.left())
        self.assertFalse(self._robot.right())

    def test_navigate_after_place(self):
        self._robot.place(0, 0, "NORTH")
        self.assertTrue(self._robot.move())
        self.assertTrue(self._robot.left())
        self.assertTrue(self._robot.right())

    def test_left(self):
        self.assertTrue(self._robot.place(0, 0, "NORTH"))
        self.assertTrue(self._robot.left())
        self.assertEqual(self._robot.f_direction, "WEST")
        self.assertTrue(self._robot.left())
        self.assertEqual(self._robot.f_direction, "SOUTH")
        self.assertTrue(self._robot.left())
        self.assertEqual(self._robot.f_direction, "EAST")
        self.assertTrue(self._robot.left())
        self.assertEqual(self._robot.f_direction, "NORTH")

    def test_right(self):
        self.assertTrue(self._robot.place(0, 0, "NORTH"))
        self.assertTrue(self._robot.right())
        self.assertEqual(self._robot.f_direction, "EAST")
        self.assertTrue(self._robot.right())
        self.assertEqual(self._robot.f_direction, "SOUTH")
        self.assertTrue(self._robot.right())
        self.assertEqual(self._robot.f_direction, "WEST")
        self.assertTrue(self._robot.right())
        self.assertEqual(self._robot.f_direction, "NORTH")

    def test_report_before_place(self):
        self.assertFalse(self._robot.report())

    def test_report_after_place(self):
        self._robot.place(0, 0, "NORTH")
        self.assertTrue(self._robot.report())
        self.assertEqual(self._robot.report(), "Output: 0,0,NORTH")


if __name__ == "__main__":
    unittest.main()
