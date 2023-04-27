import pygame


class UiGrid:
    def __init__(self, grid_width: int, grid_height: int):
        self._grid_width = grid_width
        self._grid_height = grid_height
        self.grid = self.create_ui_grid()

    def create_ui_grid(self):
        grid = [[0]*self._grid_width for _ in range(self._grid_height)]
        return grid
    
    def get_square_content(self, square_coordinates: tuple):
        return self.grid[square_coordinates[1]][square_coordinates[0]]
        

    def update_ui_grid(self, square_coordinates: tuple, click_type: str, is_mine: bool):
        # !!!!!! Most of this updating should be in a game logic class !!!!!!
        # !!!!!! This class should only be used for updating the grid  !!!!!!
        # if square is unrevealed
        if self.get_square_content(square_coordinates) == 0:
            if click_type == "rightclick":
                # changing from unrevealed to flag
                self.grid[square_coordinates[1]][square_coordinates[0]] = 1

            elif click_type == "leftclick":
                if is_mine:
                    self.grid[square_coordinates[1]][square_coordinates[0]] = 2
                else:
                    # changing from unrevealed to revealed_0
                    self.grid[square_coordinates[1]][square_coordinates[0]] = 3
            
            

        elif self.get_square_content(square_coordinates) == 1:
            if click_type == "rightclick":
                # changing from flag to unrevealed
                self.grid[square_coordinates[1]][square_coordinates[0]] = 0
        

        # return self.get_square_content(square_coordinates)

        # if the square is either a mine or a flipped tile, nothing should happen


            

