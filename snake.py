from snake_body import *

UP = 'u'
DOWN = 'd'
LEFT = 'l'
RIGHT = 'r'


class Snake:
    """
    #todo: add description
    """
    def __init__(self, length, location, orientation):
        """
        todo: edit
        A constructor for a Snake object.
        :param length:
        :param location:
        :param orientation:
        """
        self.length = length
        self.location = location
        self.orientation = orientation
        self.body_cells_list = []
        self.__head = None
        self.__tail = None
        self.color = black  # todo: delete

    def initialize_body(self, initial_head_location, initial_length):
        """
        This function initializes the snakes body (it's first orientation is always up).
        :return: None
        """
        i_row = initial_head_location[0]
        i_col = initial_head_location[1]
        for i in range(initial_length):
            new_node = SnakeNode((i_row - i, i_col))
            if i == 0:
                self.__head = new_node
                self.__tail = new_node
            else:
                self.add_to_tail(new_node)

    def connect_nodes(self, first_node, second_node):
        """
        This function connects to nodes in order to creat a new doubly-linked list.
        :param first_node:
        :param second_node:
        :return:
        """
        first_node.set_next(second_node)
        second_node.set_previous(first_node)

    def add_to_tail(self, node):
        self.connect_nodes(self.__tail, node)
        self.__tail = node

    # moving the snake

    def add_to_head(self, coordinate):
        new_head = self.snake_body.create_new_node(coordinate)
        new_head.next = self.__head
        self.__head.previous = new_head
        self.__head = new_head

    def cut_from_tail(self):
        """
        this function removes the current tail of the snake
        (the last node of the snake's body)
        """
        old_tail = self.__tail
        self.__tail = self.__tail.previous
        self.__tail.next = None
        return old_tail

        # todo: remove from body list

    # snake_moves_helpers:

    def possible_moves(self):
        """
        This function returns all possible moves based on the
        current orientation
        :return: either UP, DOWN or LEFT, RIGHT
        """
        if self.orientation in (UP, DOWN):
            return LEFT, RIGHT
        return UP, DOWN

    def next_step_coordinates(self):
        # todo: complete
        pass

    def snake_move(self, coordinate):
        self.add_to_head(coordinate)
        old_tail = self.cut_from_tail()
        self.body_cells_list.append(coordinate)
        self.body_cells_list.remove(old_tail)
        # todo: remove add to body list
