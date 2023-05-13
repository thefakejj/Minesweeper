from enums.mouse_enum import MouseEnum
from constants import (WINDOW_HEIGHT,
                       DEFAULT_BACK_TO_MENU_COORDINATES, DEFAULT_SIDE_BUTTON_IMAGE_SIZE)


class MouseEvent:
    """class for handling pygame events having to do with mouse inputs
    Attributes:
        image_size: Minesweeper's image size
        grid_width: Minesweeper's grid width
        grid_height: Minesweeper's grid height
        x_where_grid_ends: Minesweeper's grid's last x coordinate in pixels
        change_game_state: Minesweeper's change_game_state function
    """

    def __init__(self, image_size: tuple, grid_width: int, grid_height: int, x_where_grid_ends: int, change_game_state):
        """Creates a MouseEvent object and gives it attributes for the current settings of minesweeper

        Args:
            image_size (tuple): Minesweeper's image size
            grid_width (int): Minesweeper's grid width
            grid_height (int): Minesweeper's grid height
            x_where_grid_ends (int): Minesweeper's grid's last x coordinate in pixels
            change_game_state (function): Minesweeper's change_game_state function
        """

        self.image_size = image_size

        self.grid_width = grid_width
        self.grid_height = grid_height

        self.x_where_grid_ends = x_where_grid_ends

        self.change_game_state = change_game_state

    def side_button_click(self, click_coordinates: tuple):
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
                self.change_game_state(0)

    def square_click(self, event_button: int, click_coordinates: tuple,
                     first_click_has_happened: bool, start_game, grid, field_grid: list):
        """Checks if click's coordinates were within the grid.
            If they were, another method checks which square was clicked.
            Based on what square was clicked,
            corresponding methods from minesweeper and grid are called.

        Args:
            event_button (int): left click or right click, 1 for left and 3 for right
            click_coordinates (tuple): x and y coordinates of the square in pixels
            first_click_has_happened (bool): whether or not a click has happened this game
            start_game (function): Minesweeper's function for starting a game
            grid (list): Minesweeper's Grid object's grid
            field_grid (list): Minesweeper's Field object's grid
        """
        # this jungle of if-statements determines
        # whether or not the click is within grid's dimensions

        # when click is inside the grid
        if (click_coordinates[0] >= 0
                and click_coordinates[0] <= self.x_where_grid_ends):
            if click_coordinates[1] >= 0 and click_coordinates[1] <= WINDOW_HEIGHT:

                square_coordinates = self.which_square_was_clicked(
                    click_coordinates)

                if event_button == MouseEnum.LEFT_CLICK:
                    if grid.get_square_content(square_coordinates) == 1:
                        return

                    if first_click_has_happened is False:
                        start_game(square_coordinates)

                    elif field_grid[square_coordinates[1]][square_coordinates[0]] == 1:
                        self.change_game_state(3)
                        self.reveal_grid(grid, field_grid)
                        return
                grid.update_grid(square_coordinates, event_button, field_grid)

                # update and check if mine. if mine, change game state

    def which_square_was_clicked(self, click_coordinates: tuple):
        """converts click's pixel coorinates into grid coordinates

        Args:
            click_coordinates (tuple): x and y coordinates of click

        Returns:
            tuple: x and y coordinates of a square in the grid
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
            if ((click_coordinates[0] >= 0+(width*self.image_size[1]))
                    and click_coordinates[0]
                    <= 0+((width+1)*self.image_size[1])):
                square_x = width

        return (square_x, square_y)

    # for testing purposes :)
    def reveal_grid(self, grid: object, field_grid: list):
        """calls the Grid object's reveal_grid method

        Args:
            grid (object): Minesweeper's Grid object
            field_grid (list): Minesweeper's Field object's grid
        """
        grid.reveal_grid(field_grid)
