from random import randint


# 0: empty, 1: mine
# make another grid for revealed and unrevealed tiles in pygame
class Field:
    def __init__(self, width, height, first_click_coordinates: tuple):

        self.width = width
        self.height = height

        self.first_click_coordinates = first_click_coordinates

        # minesweeper has 16% of tiles as mines
        self.mine_count = (16*(self.width*self.height))//100
        self.grid = [[0]*self.width for i in range(self.height)]

        self.create_random_field()
        self.print_grid()

    def create_random_field(self):

        for _ in range(self.mine_count):
            x_coordinate = randint(0, self.width-1)
            y_coordinate = randint(0, self.height-1)

            # checks that randomised coordinates aren't
            # the same as first click's
            # and that coordinates dont have a mine
            while (self.grid[y_coordinate][x_coordinate] == 1
                   or (x_coordinate, y_coordinate) == self.first_click_coordinates):
                x_coordinate = randint(0, self.width-1)
                y_coordinate = randint(0, self.height-1)
            self.grid[y_coordinate][x_coordinate] = 1

    # this method may be unnecessary for the finished product
    # but it exists for the purpose of debugging
    def print_grid(self):
        print()
        print(self)
        print("Minesweeper grid: ")
        for row in self.grid:
            print(row)

    def __str__(self):
        return f"Field (size={self.width}x{self.height}, , mine count={self.mine_count})"
