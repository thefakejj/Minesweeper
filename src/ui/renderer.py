import pygame

from constants import DEFAULT_SIDE_BUTTON_IMAGE_SIZE, WINDOW_WIDTH, WINDOW_HEIGHT

class Renderer:
    def __init__(self, minesweeper, images, buttons):
        pygame.font.init()
        self.font = pygame.font.SysFont('Arial Black', 25)
        self.minesweeper = minesweeper
        self.images = images
        self.buttons = buttons

    def render(self):
        self.minesweeper.surface.fill(self.minesweeper.bg_color)
        self.draw_grid()
        self.draw_side_buttons()
        if self.minesweeper.game_state == 3:
            self.draw_text("GAME OVER!!!")
        pygame.display.flip()

    def draw_grid(self):
        for y in range(self.minesweeper.grid_height):
            for x in range(self.minesweeper.grid_width):
                square = self.minesweeper.ui_grid.grid[y][x]
                # every image is 100x100 pixels, so a drawn square should always be scaled from that size
                self.minesweeper.surface.blit(self.images[square],
                                   (x * self.minesweeper.image_size[0], y * self.minesweeper.image_size[1]))

    def draw_side_buttons(self):
        for button_index, button in enumerate(self.buttons):
            (self.minesweeper.surface.blit(button,
            (WINDOW_WIDTH - DEFAULT_SIDE_BUTTON_IMAGE_SIZE[0], button_index * DEFAULT_SIDE_BUTTON_IMAGE_SIZE[1])))

    def draw_text(self, text: str):
        text_surface = self.font.render(text, True, (0, 0, 0))

        self.minesweeper.surface.blit(text_surface, (WINDOW_WIDTH - text_surface.get_width(), WINDOW_HEIGHT - text_surface.get_height()))