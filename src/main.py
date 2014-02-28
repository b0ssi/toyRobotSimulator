#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on 28/02/2014

@author: Frieder Czeschla
"""

import trs.actors
import trs.readers
import os
import sys


class Main(object):
    """
    This class initializes the application, depending on its parameters with
    standard-input or a text-file as its source of commands.
    """

    def _display_help(self):
        """
        Prints out the application's help and parameter-reference.
        """
        out = "\n"
        out += "Usage:\n"
        out += " trs [inputFile]\n"
        out += "\n"
        out += " If not inputFile is given, commands will be read from "\
               "standard input.\n"
        out += "\n"
        out += " inputFile:\tA text-file containing a list of commands.\n"
        out += "\n"
        out += "Available Commands:\n"
        out += "\n"
        out += " PLACE X,Y,F:\tPlace the robot onto the board at X,Y,F\n"
        out += "\t\t The origin 0,0 is the SOUTH WEST most corner of the "\
               "board.\n"
        out += "\t\t X: int: x-coordinate\n"
        out += "\t\t Y: int: y-coordinate\n"
        out += "\t\t F: (NORTH|SOUTH|EAST|WEST): The facing-direction\n"
        out += " MOVE:\t\tMove the robot by one field forward into the"\
               "direction it faces.\n"
        out += " LEFT:\t\tTurn the robot leftwards by 90 degrees.\n"
        out += " RIGHT:\t\tTurn the robot rightwards by 90 degrees.\n"
        out += " REPORT:\tOutput a position/direction report in the form of "\
               "<X,Y,F>.\n"
        print(out)

    def run(self):
        """
        Initializes the application depending on passed command-line
        parameters.
        """
        # instantiate actors
        board = trs.actors.Board(5, 5)
        robot = trs.actors.Robot(board)
        # check for parameters
        if len(sys.argv) < 2:
            # initiate with standard-input for command-entry
            cmds_reader = trs.readers.CmdsReaderSIn(robot)
            cmds_reader.run()
        elif len(sys.argv) == 2:
            # initiate with file from parameters as command-source
            file_path_abs = os.path.realpath(os.path.abspath(sys.argv[1]))
            if os.path.isfile(file_path_abs):
                cmds_reader = trs.readers.CmdsReaderFIn(robot, file_path_abs)
                cmds_reader.run()
            else:
                # invalid parameters
                self._display_help()
        elif len(sys.argv) > 2:
            # invalid parameter count
            self._display_help()


# initialize runtime
if __name__ == "__main__":
    main = Main()
    main.run()
