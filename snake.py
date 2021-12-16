UP = 'u'
DOWN = 'd'
LEFT = 'l'
RIGHT = 'r'

from snake_body import *

class Snake:
    """
    #todo: add description
    """
    def __init__(self, length, location, orientation, coordinates_list):
        """
        todo: edit
        A constructor for a Snake object.
        :param length:
        :param location:
        :param orientation:
        :param coordinates_list:
        """
        self.length = length
        self.location = location
        self.orientation = orientation
        self.coordinates_list = coordinates_list

    def snake_coordinates(self):
        """
        :return:
        """

    def possible_moves(self):
        """
        This function returns all possible moves based on the
        current orientation
        :return: either UP, DOWN or LEFT, RIGHT
        """
        if self.orientation in (UP, DOWN):
            return LEFT, RIGHT
        return UP, DOWN

    def change_direction(self, new_direction):
        self.orientation = new_direction

    def next_step_coordinates(self):
        if self.orientation == DOWN:
            self.location = self.location[0]

