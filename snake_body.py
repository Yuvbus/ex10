class SnakeBody:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0

    def create_new_node(self, coordinate):
        self.__data = coordinate
        self.__previous = None
        self.__next = None

    def add_to_head(self, coordinate):
        new_head = self.create_new_node(coordinate)
        new_head.next = self.__head
        self.__head.previous = new_head
        self.__head = new_head

    def cut_from_tail(self):
        """
        this function removes the current tail of the snake
        (the last node of the snake's body)
        """
        self.__tail = self.__tail.previous
        self.__tail.next = None
