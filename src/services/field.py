from random import randint


# 0: empty, 1: mine
# make another grid for revealed and unrevealed tiles in pygame
class Field:
    def __init__(self, scale: int):
        # something randint, should maybe take input from pygame to ensure the first tile is empty
        self.scale = scale
        # minesweeper has 16% of tiles as mines
        self.mine_count = (16*(scale*scale))//100
        self.grid = [[0]*self.scale for i in range(self.scale)]
        self.create_random_field()
        # first click's x and y could be object attributes

    def create_random_field(self):

        for i in range(self.mine_count):
            # firstclick_x = some_input_x
            # firstclick_y = some_input_y

            x_coordinate = randint(0, self.scale-1)
            y_coordinate = randint(0, self.scale-1)

            # when the pygame functinality is added
            # the while loop should also check that the first square that was clicked is not a mine
            while self.grid[y_coordinate][x_coordinate] == 1:
                x_coordinate = randint(0, self.scale-1)
                y_coordinate = randint(0, self.scale-1)
            self.grid[y_coordinate][x_coordinate] = 1

    # this method may be unnecessary for the finished product
    # but it exists for the purpose of debugging
    def print_grid(self):
        print()
        print(self)
        tulostus = str(self)
        print("tulostus:", tulostus)
        print("Minesweeper grid: ")
        for row in self.grid:
            print(row)

    def __str__(self):
        return f"Field (scale={self.scale}, mine count={self.mine_count})"

# sample field
# around 16%  of the tiles should have a mine
# so in this 64-tile grid, there are 10 mines and 54 empty tiles