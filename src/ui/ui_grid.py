from enums.ui_grid_enum import UiGridEnum


class UiGrid:
    """class that deals with the visible grid
    """

    def __init__(self, grid_width: int, grid_height: int):
        """creates an ui_grid object, including creating a list full of zeros

        Args:
            grid_width (int): width of the minesweeper grid
            grid_height (int): height of the minesweeper grid
        """
        self._grid_width = grid_width
        self._grid_height = grid_height
        self.grid = self.create_ui_grid()
        
        self._revealed_tiles = 0
        self._mine_count = (16*(self._grid_width*self._grid_height))//100

    def create_ui_grid(self):
        """creates a list that represents the visible grid

        Returns:
            list: grid full of zeros (unrevealed tiles)
        """
        grid = [[0]*self._grid_width for _ in range(self._grid_height)]
        return grid

    def get_square_content(self, square_coordinates: tuple):
        """returns the content of a specific tile in the visible grid

        Args:
            square_coordinates (tuple): x and y coordinates of a square

        Returns:
            (UiGridEnum/int): the square's contents
        """
        square_x = square_coordinates[0]
        square_y = square_coordinates[1]
        return self.grid[square_y][square_x]

    def set_square_content(self, square_coordinates, content):
        """changes the content of a specified square

        Args:
            square_coordinates (tuple): x and y coordinates of a square
            content (UiGridEnum/int): the content that the square will be set to
        """
        square_x = square_coordinates[0]
        square_y = square_coordinates[1]
        self.grid[square_y][square_x] = content

    def update_ui_grid(self, square_coordinates: tuple, click_type: str, nearby_mines: int):
        """updates the grid

        Args:
            square_coordinates (tuple): x and y coordinates of a square
            click_type (str): specifies whether the click event used a left click or a right click
            nearby_mines (int): the amount of mines surrounding the square
        """
        # !!!!!! Most of this updating should be in a game logic class !!!!!!
        # !!!!!! This class should only be used for updating the grid  !!!!!!
        # if square is unrevealed
        if self.get_square_content(square_coordinates) == UiGridEnum.UNREVEALED_TILE.value:
            if click_type == "rightclick":
                # changing from unrevealed to flag
                self.set_square_content(
                    square_coordinates, UiGridEnum.FLAG.value)

            elif click_type == "leftclick":
                if nearby_mines == -1:
                    self.set_square_content(
                        square_coordinates, UiGridEnum.MINE.value)
                else:
                    # changing from unrevealed to the amount of mines
                    self.set_square_content(
                        square_coordinates, 3 + nearby_mines)
                    self._revealed_tiles += 1

        elif self.get_square_content(square_coordinates) == UiGridEnum.FLAG.value:
            if click_type == "rightclick":
                # changing from flag to unrevealed
                self.set_square_content(
                    square_coordinates, UiGridEnum.UNREVEALED_TILE.value)

        # if the square is either a mine or a flipped tile, nothing should happen

    def check_if_enough_squares_flipped(self):
        return self._revealed_tiles >= (self._grid_width*self._grid_height) - self._mine_count
                    