#todo: change the file's name to snake node.

class SnakeNode:
    """
    #todo: add description
    """

    def __init__(self, coordinate):
        """
        This function initializes an independent node.
        :param coordinate: the coordinates of the node's current cell.
        """
        self.__data = coordinate
        self.__previous = None
        self.__next = None

    def set_previous(self, new_previous):
        """
        This function sets a new previous to the current node.
        :param new_previous: a SnakeNode-type object which will be the current node's previous.
        :return: None
        """
        self.__previous = new_previous

    def set_next(self, new_next):
        """
        This function sets a new next to the current node.
        :param new_next: a SnakeNode-type object which will be the current node's next.
        :return: None
        """
        self.__next = new_next

    def get_previous(self):
        #  todo: delete
        pass

    def get_next(self):
        #  todo: delete
        pass
