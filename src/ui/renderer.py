import pygame

from constants import (DEFAULT_SIDE_BUTTON_IMAGE_SIZE, WINDOW_WIDTH, WINDOW_HEIGHT,
                       LEADERBOARD_NAME_CELL_SIZE,
                       LEADERBOARD_ROW_SIZE, LEADERBOARD_SIZE)


class Renderer:
    """class responsible for drawing the screen
    Attributes:
        font: the font that is used by text in the game view
        minesweeper: a Minesweeper object
        images: list of tile images
        buttons: list of side button images
        image_size: size of the tile images after scaling
    """

    def __init__(self, minesweeper, images: list, buttons: list, image_size: tuple):
        """creates a renderer object

        Args:
            minesweeper (object): gives the minesweeper object to renderer
            images (list): tile images
            buttons (list): side button images
            image_size (tuple): size of the tile images after scaling
        """
        pygame.font.init()
        self.font = pygame.font.SysFont('FreeSans', WINDOW_HEIGHT//30)
        self.minesweeper = minesweeper
        self.images = images
        self.buttons = buttons
        self.image_size = image_size

    def render(self):
        """updates the entire screen in game
        """
        self.minesweeper.surface.fill(self.minesweeper.bg_color)
        if self.minesweeper.game_state == 1:
            self.draw_grid()
            self.draw_text("Click to start")
            self.draw_timer()

        elif self.minesweeper.game_state == 2:
            self.draw_grid()
            self.draw_text("")
            self.draw_timer()

        elif self.minesweeper.game_state == 3:
            self.draw_grid()
            self.draw_text("GAME OVER!!!")
            self.draw_timer()

        elif self.minesweeper.game_state == 4:
            self.draw_grid()
            self.draw_text("YOU WIN!!!")
            self.draw_timer()

        elif self.minesweeper.game_state == 5:
            self.draw_leaderboard()

        self.draw_side_buttons()
        pygame.display.flip()

    def draw_grid(self):
        """draws the minesweeper grid based on the Grid object received from the minesweeper class
        """
        for y in range(self.minesweeper.grid_height):
            for x in range(self.minesweeper.grid_width):
                square = self.minesweeper.grid.grid[y][x]
                self.minesweeper.surface.blit(self.images[square],
                                              (x * self.image_size[0], y * self.image_size[1]))

    def draw_leaderboard(self):
        """draws the leaderboard view based on the leaderboard object
           received from the minesweeper class
        """
        table = self.minesweeper.leaderboard.grid_leaderboard(
            (self.minesweeper.grid_width, self.minesweeper.grid_height))

        tablefont = pygame.font.SysFont('FreeSans', WINDOW_HEIGHT//20)

        table_surface = pygame.Surface(
            (LEADERBOARD_SIZE[0], LEADERBOARD_SIZE[1]))
        table_surface.fill((0, 0, 0))
        table_surface.set_colorkey((0, 0, 0))

        table_header_surface = tablefont.render(
            f"{self.minesweeper.grid_width}x{self.minesweeper.grid_height}", False, (255, 255, 255))

        table_surface.blit(table_header_surface,
                           (table_surface.get_width()//2 - table_header_surface.get_width()//2,
                            WINDOW_HEIGHT*0.05))

        # chatgpt | idea to create row surfaces list
        row_surfaces = []
        for _, row in enumerate(table):
            # name
            name_surface = tablefont.render(
                str(row[0]), False, (255, 255, 255))

            # time
            time_surface = tablefont.render(
                str(row[1]), False, (255, 255, 255))

            # chatgpt | creating a specific surface for the current row
            # and blitting the surfaces name and time onto it
            row_surface = pygame.Surface(
                (LEADERBOARD_SIZE[0], LEADERBOARD_ROW_SIZE[1]))
            row_surface.blits(
                [(name_surface, (0, 0)), (time_surface, (LEADERBOARD_NAME_CELL_SIZE[0], 0))])

            # chatgpt | appending the created row to the list
            row_surfaces.append(row_surface)

        # chatgpt | blitting rows onto surface
        # (though I did realise that using blits was better...)
        row_positions = ([(row_surface, (0, WINDOW_HEIGHT*0.05
                                         + (index + 1) * LEADERBOARD_ROW_SIZE[1]))
                          for index, row_surface in enumerate(row_surfaces)])
        table_surface.blits(row_positions)

        self.minesweeper.surface.blit(
            table_surface, ((WINDOW_WIDTH // 2 - table_surface.get_width() // 2), 0))

    def draw_timer(self):
        """draws the timer based on the Clock object received from the minesweeper class
        """
        time = str(self.minesweeper.clock.get_elapsed_time_in_seconds())
        timer_surface = self.font.render(time, True, (0, 0, 0))
        self.minesweeper.surface.blit(
            timer_surface, (WINDOW_WIDTH - DEFAULT_SIDE_BUTTON_IMAGE_SIZE[0],
                            DEFAULT_SIDE_BUTTON_IMAGE_SIZE[1] + timer_surface.get_height()))

    def draw_side_buttons(self):
        """draws the side buttons (only back to menu)
        """
        for button_index, button in enumerate(self.buttons):
            (self.minesweeper.surface.blit(button,
                                           (WINDOW_WIDTH - DEFAULT_SIDE_BUTTON_IMAGE_SIZE[0],
                                            button_index * DEFAULT_SIDE_BUTTON_IMAGE_SIZE[1])))

    def draw_text(self, text: str):
        """draws text on the screen upon certain scenarios like revealing a mine

        Args:
            text (str): the text that should be displayed, eg. "Game over" when mine is revealed
        """
        text_surface = self.font.render(text, True, (0, 0, 0))

        self.minesweeper.surface.blit(
            text_surface, (WINDOW_WIDTH*0.99 - text_surface.get_width(),
                           WINDOW_HEIGHT*0.75 - text_surface.get_height()))
