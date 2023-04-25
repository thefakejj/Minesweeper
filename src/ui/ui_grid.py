import pygame


class UiGrid:
    def __init__(self, grid_width: int, grid_height: int):
        self._grid_width = grid_width
        self._grid_height = grid_height
        self.grid = self.create_ui_grid()

    def create_ui_grid(self):
        grid = [[0]*self._grid_width for i in range(self._grid_height)]
        return grid

    def update_ui_grid(self, x_coordinate, y_coordinate, type):
        square_content = self.grid[y_coordinate][x_coordinate]

        # if square is unrevealed or a flag
        if square_content == 0:
            if type == 2:
                # changing from unrevealed to flag
                self.grid[y_coordinate][x_coordinate] = 1

        elif square_content == 1:
            if type == 2:
                # changing from flag to unrevealed
                self.grid[y_coordinate][x_coordinate] = 0
