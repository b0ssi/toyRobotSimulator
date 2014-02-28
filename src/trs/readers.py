# -*- coding: utf-8 -*-
'''
Created on 28/02/2014

@author: Frieder Czeschla
'''

import os


class CmdsReader(object):
    """
    Superclass for CmdsReaderSIn, CmdsReaderFIn. Routes and executes the
    commands read in by its subclasses.
    """
    _robot = None

    def __init__(self, robot):
        """
        """
        self._robot = robot

    def _exec_cmd(self, cmd, verbose=True):
        """
        Routes the command `cmd` to its corresponding method call.
        """
        # unpack command
        cmd_base = cmd.split(" ")[0]
        cmd_params = None
        if len(cmd.split(" ")) > 1:
            cmd_params = cmd.split(" ")[1].split(",")
        out = None
        # route command
        if cmd_base == "PLACE":
            if cmd_params != None:
                try:
                    cmd_params[0] = int(cmd_params[0])
                    cmd_params[1] = int(cmd_params[1])
                    if cmd_params[2] in ("NORTH", "SOUTH", "EAST", "WEST"):
                        out = self._robot.place(cmd_params[0],
                                                cmd_params[1],
                                                cmd_params[2])
                except Exception as e:
                    pass
        elif cmd_base == "MOVE":
            out = self._robot.move()
        elif cmd_base == "LEFT":
            out = self._robot.left()
        elif cmd_base == "RIGHT":
            out = self._robot.right()
        elif cmd_base == "REPORT":
            out = self._robot.report()
        if out not in (None, True, False) and\
            verbose == True:
            print(out)


class CmdsReaderSIn(CmdsReader):
    """
    Provides an input loop/command dispatcher for the standard-input.
    """

    def __init__(self, robot):
        super(CmdsReaderSIn, self).__init__(robot)

    def run(self):
        """
        Initializes the standard-input loop and dispatches commands.
        """
        input_str = None
        while input_str != "exit":
            try:
                input_str = raw_input("")
            except NameError:
                input_str = input("")
            self._exec_cmd(input_str)
        return True


class CmdsReaderFIn(CmdsReader):
    """
    Provides an input loop/command dispatcher for file-input.
    """
    _file_path_abs = None

    def __init__(self, robot, file_path_abs):
        super(CmdsReaderFIn, self).__init__(robot)

        self._file_path_abs = file_path_abs

    def run(self, verbose=True):
        """
        Reads the file from the file path this class has been instantiated with
        line by line and dispatches each line as a command.
        """
        if os.path.isfile(self._file_path_abs):
            with open(self._file_path_abs, "r") as f:
                for line in f.readlines():
                    if line[-1] == "\n":
                        line = line[:-1]
                    if verbose == True:
                        print(line)
                    self._exec_cmd(line, verbose)
                return True
        else:
            return False
