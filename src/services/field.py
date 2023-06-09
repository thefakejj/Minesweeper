from random import randint


# 0: empty, 1: mine
class Field:
    """class for the backend field, which holds the locations of the mines
    Attributes:
        width: grid width
        height: grid height
        _mine_count: amount of mines that need to be generated
        grid: 1 = mine, 0: empty
    """

    def __init__(self, width: int, height: int):
        """creates a field object and makes an empty grid.
            Minesweeper has 16% mines, so an attribute is created for that

        Args:
            width (int): wanted grid width
            height (int): wanted grid height
        """

        self.width = width
        self.height = height

        self._mine_count = (16*(self.width*self.height))//100
        self.grid = [[0]*self.width for _ in range(self.height)]

    def create_random_field(self, first_click_coordinates: tuple):
        """creates a randomized field, which makes sure that the clicked tile has no mine

        Args:
            first_click_coordinates (tuple): grid coordinates for the player's first click
        """

        for _ in range(self._mine_count):
            x_coordinate = randint(0, self.width-1)
            y_coordinate = randint(0, self.height-1)

            # checks that randomised coordinates aren't
            # the same as first click's
            # and that coordinates dont have a mine
            while (self.grid[y_coordinate][x_coordinate] == 1
                   or (x_coordinate, y_coordinate) == first_click_coordinates):
                x_coordinate = randint(0, self.width-1)
                y_coordinate = randint(0, self.height-1)
            self.grid[y_coordinate][x_coordinate] = 1
