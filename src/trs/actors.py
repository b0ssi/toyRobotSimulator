'''
Created on 28/02/2014

@author: Frieder Czeschla
'''


class Robot(object):
    """
    """
    _board = None
    pos_x = None
    pos_y = None
    f_direction = None

    def __init__(self, board):
        """
        """
        self._board = board

    @property
    def _has_been_placed(self):
        if self.pos_x != None and\
            self.pos_y != None and\
            self.f_direction != None:
            return True
        else:
            return False

    def place(self, x, y, f):
        if 0 <= x < self._board.width and\
            0 <= y < self._board.height and\
            f in ["NORTH", "SOUTH", "EAST", "WEST"]:
            self.pos_x = x
            self.pos_y = y
            self.f_direction = f

            return True
        else:
            return False

    def move(self):
        if self._has_been_placed == True:
            x_new = self.pos_x
            y_new = self.pos_y
            # calculate new hypothetical position
            if self.f_direction == "NORTH":
                y_new = self.pos_y + 1
            elif self.f_direction == "SOUTH":
                y_new = self.pos_y - 1
            elif self.f_direction == "EAST":
                x_new = self.pos_x + 1
            elif self.f_direction == "WEST":
                x_new = self.pos_x - 1
            # check validity of new position and set if valid
            if 0 <= x_new < self._board.width and\
                0 <= y_new < self._board.height:
                self.pos_x = x_new
                self.pos_y = y_new
                return True
            else:
                return False
        else:
            return False

    def left(self):
        if self._has_been_placed == True:
            directions = ["NORTH", "EAST", "SOUTH", "WEST"]
            new_direction_index = directions.index(self.f_direction) - 1
            if new_direction_index < 0: new_direction_index = len(directions) - 1
            self.f_direction = directions[new_direction_index]
            return True
        else:
            return False

    def right(self):
        if self._has_been_placed == True:
            directions = ["NORTH", "EAST", "SOUTH", "WEST"]
            new_direction_index = directions.index(self.f_direction) + 1
            if new_direction_index > 3: new_direction_index = 0
            self.f_direction = directions[new_direction_index]
            return True
        else:
            return False

    def report(self):
        if self._has_been_placed == True:
            return "Output: %d,%d,%s" % (self.pos_x,
                                        self.pos_y,
                                        self.f_direction)
        else:
            return False


class Board(object):
    """
    """
    width = None
    height = None

    def __init__(self, width, height):
        self.width = width
        self.height = height
