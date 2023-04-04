from random import randint


#0: empty, 1: bomb                                                 , make another grid for revealed and unrevealed tiles
class Field:
    def __init__(self, scale: int):
        #something randint, should maybe take input from pygame to ensure the first tile is empty
        #additionally, you could have an array full of None to begin with, which is then filled accordingly after the first click
        self.scale = scale
        #minesweeper has 16% of tiles as mines
        self.mine_count = (16*(scale*scale))//100
        self.create_random_field()

    def create_random_field(self):
        self.grid = [[0]*self.scale for i in range(self.scale)]

        for i in range(self.mine_count):
            x = randint(0, self.scale-1)
            y = randint(0, self.scale-1)

            while self.grid[y][x] == 1:
                x = randint(0, self.scale-1)
                y = randint(0, self.scale-1)
            self.grid[y][x] = 1

        
        for row in self.grid:
            print(row)


    def __str__(self):
        return f"Field (scale={self.scale}, mine count={self.mine_count})"

#sample field
#around 16%  of the tiles should have a mine, so in this 64-tile grid, there are 10 mines and 54 empty tiles
sample_field_array = [
[0, 0, 0, 0, 1, 0, 0, 0],
[0, 0, 1, 0, 0, 0, 0, 0],
[1, 0, 0, 0, 0, 0, 1, 0],
[0, 0, 1, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 1, 0, 0, 0],
[0, 0, 0, 0, 0, 1, 0, 0],
[0, 1, 1, 0, 0, 0, 1, 0],
[0, 0, 0, 0, 0, 0, 0, 0]
]