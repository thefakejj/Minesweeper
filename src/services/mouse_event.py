from enums.mouse_enum import MouseEnum
from constants import (WINDOW_HEIGHT,
                       DEFAULT_BACK_TO_MENU_COORDINATES, DEFAULT_SIDE_BUTTON_IMAGE_SIZE)
from services.check_if_mine import square_is_mine, nearby_mines


class MouseEvent:
    """class for handling pygame events having to do with mouse inputs and game logic
    """

    def __init__(self, minesweeper, image_size):
        """creates mouse_event object

        Args:
            minesweeper (object): gives minesweeper object to the class
        """

        self.image_size = image_size

        self.minesweeper = minesweeper

        self.grid_width = self.minesweeper.grid_width
        self.grid_height = self.minesweeper.grid_height

        self.x_where_grid_starts = self.minesweeper.x_where_grid_starts
        self.x_where_grid_ends = self.minesweeper.x_where_grid_ends

        self.change_game_state = self.minesweeper.change_game_state

    def side_button_click(self, click_coordinates):
        """Checks if click's coordinates in the window are within a side button's limits.
            If they are, a corresponding minesweeper function is called

        Args:
            click_coordinates (tuple): x and y coordinates of the square in pixels
        """
        button_coordinates_x, button_coordinates_y = DEFAULT_BACK_TO_MENU_COORDINATES
        button_width, button_height = DEFAULT_SIDE_BUTTON_IMAGE_SIZE
        if (click_coordinates[0] >= button_coordinates_x
                and click_coordinates[0] <= button_coordinates_x+button_width):

            if (click_coordinates[1] >= button_coordinates_y
                    and click_coordinates[1] <= button_coordinates_y + button_height):
                self.minesweeper.change_game_state(0)

    def square_click(self, event_button, click_coordinates,
                     first_click_has_happened, start_game, grid, field_grid):
        """Checks if click's coordinates were within the grid.
            If they were, another method checks which square was clicked.
            Based on what square was clicked, corresponding minesweeper methods are called.

        Args:
            event_button (int): left click or right click, 1 for left and 3 for right
            click_coordinates (tuple): x and y coordinates of the square in pixels
            first_click_has_happened (bool): whether or not a click has happened this game
            start_game (function): minesweeper's function for starting a game
            grid (list): minesweeper's ui_grid object
            field_grid (list): minesweeper's field_grid object
        """
        # this jungle of if-statements determines
        # whether or not the click is within grid's dimensions

        # when click is inside the grid
        if (click_coordinates[0] >= self.x_where_grid_starts
                and click_coordinates[0] <= self.x_where_grid_ends):
            if click_coordinates[1] >= 0 and click_coordinates[1] <= WINDOW_HEIGHT:

                square_coordinates = self.which_square_was_clicked(
                    click_coordinates)

                click_type = None

                if event_button == MouseEnum.RIGHT_CLICK:
                    click_type = "rightclick"

                if event_button == MouseEnum.LEFT_CLICK:
                    if grid.get_square_content(square_coordinates) == 1:
                        return

                    click_type = "leftclick"
                    if first_click_has_happened is False:
                        start_game(square_coordinates)

                    elif square_is_mine(square_coordinates, field_grid):
                        self.change_game_state(3)

                # update and check if mine. if mine, change game state
                grid.update_ui_grid(square_coordinates, click_type, nearby_mines(
                    square_coordinates, field_grid))

        # when click is outside the grid
        else:
            return

    def which_square_was_clicked(self, click_coordinates):
        """converts click's pixel coorinates into grid coordinates

        Args:
            click_coordinates (tuple): x and y coordinates of click

        Returns:
            tuple: x and y coordinates of a square in ui_grid
        """
        # y coordinates
        for height in range(self.grid_height):
            # grid will always start at y=0 and end at y = WINDOW_HEIGHT
            if (click_coordinates[1] >= 0+(height*self.image_size[1])
                    and click_coordinates[1] <= 0+((height+1)*self.image_size[1])):
                square_y = height

        # x coordinates
        for width in range(self.grid_width):
            # x-coordinates are given from the scaling module
            if ((click_coordinates[0] >= self.x_where_grid_starts+(width*self.image_size[1]))
                    and click_coordinates[0] <= self.x_where_grid_starts+((width+1)*self.image_size[1])):
                square_x = width

        return (square_x, square_y)

    # fake mouse events to reveal everything
    def reveal_grid(self, grid, field_grid):
        for row_index, row in enumerate(grid.grid):
            for square_index, square in enumerate(grid.grid[row_index]):
                square_content = grid.get_square_content((square_index, row_index))
                if square_content == 1:
                    continue
                elif square_content >= 3:
                    continue
                grid.update_ui_grid((square_index, row_index),
                                    "leftclick",
                                    nearby_mines((square_index, row_index), field_grid.grid))