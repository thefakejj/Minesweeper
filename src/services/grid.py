from enums.grid_enum import GridEnum
from enums.mouse_enum import MouseEnum


class Grid:
    """class that deals with the visible grid
    """

    def __init__(self, grid_width: int, grid_height: int):
        """creates an grid object, including creating a list full of zeros

        Args:
            grid_width (int): width of the minesweeper grid
            grid_height (int): height of the minesweeper grid
        """
        self._grid_width = grid_width
        self._grid_height = grid_height
        self.grid = self.create_grid()

        self.revealed_tiles = 0
        self._mine_count = (16*(self._grid_width*self._grid_height))//100

    def create_grid(self):
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
            (GridEnum/int): the square's contents
        """
        square_x = square_coordinates[0]
        square_y = square_coordinates[1]
        return self.grid[square_y][square_x]

    def set_square_content(self, square_coordinates, content):
        """changes the content of a specified square

        Args:
            square_coordinates (tuple): x and y coordinates of a square
            content (GridEnum/int): the content that the square will be set to
        """
        square_x = square_coordinates[0]
        square_y = square_coordinates[1]
        self.grid[square_y][square_x] = content

    def update_grid(self, square_coordinates: tuple, event_button: int, field_grid: list):
        """updates the grid

        Args:
            square_coordinates (tuple): x and y coordinates of a square
            event_button (int): specifies whether the click event used a left click or a right click
            nearby_mines (int): the amount of mines surrounding the square
        """
        # if square is unrevealed
        nearby_mines = self.count_nearby_mines(square_coordinates, field_grid)

        if event_button == MouseEnum.LEFT_CLICK.value:
            if self.get_square_content(square_coordinates) == GridEnum.UNREVEALED_TILE.value:
                # changing from unrevealed to mine
                if nearby_mines == -1:
                    self.set_square_content(
                        square_coordinates, GridEnum.MINE.value)
                else:
                    # changing from unrevealed to the amount of mines
                    self.set_square_content(
                        square_coordinates, 3 + nearby_mines)
                    self.revealed_tiles += 1

        if event_button == MouseEnum.RIGHT_CLICK.value:
            if self.get_square_content(square_coordinates) == GridEnum.UNREVEALED_TILE.value:
                # changing from unrevealed to flag
                self.set_square_content(
                    square_coordinates, GridEnum.FLAG.value)
                return
            if self.get_square_content(square_coordinates) == GridEnum.FLAG.value:
                # changing from flag to unrevealed
                self.set_square_content(
                    square_coordinates, GridEnum.UNREVEALED_TILE.value)
                return

        # if the square is either a mine or a flipped tile, nothing should happen

    def check_if_enough_squares_flipped(self):
        return self.revealed_tiles >= (self._grid_width*self._grid_height) - self._mine_count

    def count_nearby_mines(self, square_coordinates: tuple, field_grid: list):
        """algorhithm for counting mines around the square

        Args:
            square_coordinates (tuple): x and y coordinates of the square
            field_grid (list): the field object's grid

        Returns:
            int: amount of mines surrounding the square
        """
        if field_grid[square_coordinates[1]][square_coordinates[0]] == 1:
            return -1

        mines = 0
        for j in range(square_coordinates[1]-1, square_coordinates[1]+2):
            for i in range(square_coordinates[0]-1, square_coordinates[0]+2):
                if i < 0 or j < 0 or j >= len(field_grid) or i >= len(field_grid[0]):
                    continue
                if field_grid[j][i] == 1:
                    mines += 1
        return mines


    def reveal_grid(self, field_grid: list):
        for row_index, _ in enumerate(self.grid):
            for square_index, _ in enumerate(self.grid[row_index]):
                square_content = self.get_square_content(
                    (square_index, row_index))
                if square_content == 1 or square_content >= 3:
                    continue
                self.update_grid((square_index, row_index),
                                 MouseEnum.LEFT_CLICK.value, field_grid)
