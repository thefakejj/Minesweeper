from enums.ui_grid_enum import UiGridEnum

class UiGrid:
    def __init__(self, grid_width: int, grid_height: int):
        self._grid_width = grid_width
        self._grid_height = grid_height
        self.grid = self.create_ui_grid()

    def create_ui_grid(self):
        grid = [[0]*self._grid_width for _ in range(self._grid_height)]
        return grid
    
    def get_square_content(self, square_coordinates: tuple):
        square_x = square_coordinates[0]
        square_y = square_coordinates[1]
        return self.grid[square_y][square_x]
    
    def set_square_content(self, square_coordinates, content):
        square_x = square_coordinates[0]
        square_y = square_coordinates[1]
        self.grid[square_y][square_x] = content
        # print("ui gridi: \n")
        # for y in range(len(self.grid)):
        #     for x in range(len(self.grid[y])):
        #         print(self.grid[y][x])


    def update_ui_grid(self, square_coordinates: tuple, click_type: str, is_mine: bool):
        # !!!!!! Most of this updating should be in a game logic class !!!!!!
        # !!!!!! This class should only be used for updating the grid  !!!!!!
        # if square is unrevealed
        if self.get_square_content(square_coordinates) == UiGridEnum.UNREVEALED_TILE.value:
            if click_type == "rightclick":
                # changing from unrevealed to flag
                self.set_square_content(square_coordinates, UiGridEnum.FLAG.value)
                return True

            elif click_type == "leftclick":
                if is_mine is True:
                    self.set_square_content(square_coordinates, UiGridEnum.MINE.value)
                    return True
                else:
                    # changing from unrevealed to revealed_0
                    self.set_square_content(square_coordinates, UiGridEnum.REVEALED_0.value)
                    return True

        elif self.get_square_content(square_coordinates) == UiGridEnum.FLAG.value:
            if click_type == "rightclick":
                # changing from flag to unrevealed
                self.set_square_content(square_coordinates, UiGridEnum.UNREVEALED_TILE.value)
                return True

        # if the square is either a mine or a flipped tile, nothing should happen
