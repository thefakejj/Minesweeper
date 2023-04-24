import pygame


class UiGrid:
    def __init__(self, grid_width: int, grid_height: int):
        self._grid_width = grid_width
        self._grid_height = grid_height
        self.grid = self.create_ui_grid()

    def create_ui_grid(self):
        grid = [[0]*self._grid_width for i in range(self._grid_height)]
        return grid
