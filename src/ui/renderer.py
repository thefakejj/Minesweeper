import pygame

from constants import DEFAULT_SIDE_BUTTON_IMAGE_SIZE, WINDOW_WIDTH, WINDOW_HEIGHT


class Renderer:
    """class responsible for drawing the screen
    """

    def __init__(self, minesweeper, images, buttons, image_size):
        """creates a renderer object

        Args:
            minesweeper (Minesweeper object): gives the created minesweeper object to the renderer
            images (list): tile images
            buttons (list): side button images
        """
        pygame.font.init()
        self.font = pygame.font.SysFont('Arial Black', 25)
        self.minesweeper = minesweeper
        self.images = images
        self.buttons = buttons
        self.image_size = image_size

    def render(self):
        """updates the entire screen in game
        """
        self.minesweeper.surface.fill(self.minesweeper.bg_color)
        self.draw_grid()
        self.draw_side_buttons()
        if self.minesweeper.game_state == 3:
            self.draw_text("GAME OVER!!!")
        pygame.display.flip()

    def draw_grid(self):
        """draws the minesweeper grid based on the UiGrid object received from the minesweeper class
        """
        for y in range(self.minesweeper.grid_height):
            for x in range(self.minesweeper.grid_width):
                square = self.minesweeper.ui_grid.grid[y][x]
                # every image is 100x100 pixels, so a drawn square should always be scaled from that size
                self.minesweeper.surface.blit(self.images[square],
                                              (x * self.image_size[0], y * self.image_size[1]))

    def draw_side_buttons(self):
        """draws the side buttons (only back to menu)
        """
        for button_index, button in enumerate(self.buttons):
            (self.minesweeper.surface.blit(button,
                                           (WINDOW_WIDTH - DEFAULT_SIDE_BUTTON_IMAGE_SIZE[0], button_index * DEFAULT_SIDE_BUTTON_IMAGE_SIZE[1])))

    def draw_text(self, text: str):
        """draws text on the screen upon certain scenarios like revealing a mine

        Args:
            text (str): the text that should be displayed, eg. "Game over" when mine is revealed
        """
        text_surface = self.font.render(text, True, (0, 0, 0))

        self.minesweeper.surface.blit(
            text_surface, (WINDOW_WIDTH - text_surface.get_width(), WINDOW_HEIGHT - text_surface.get_height()))
