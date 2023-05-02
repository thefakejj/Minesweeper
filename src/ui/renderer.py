import pygame
from constants import DEFAULT_SIDE_BUTTON_IMAGE_SIZE, WINDOW_WIDTH

class Renderer:
    def __init__(self, surface, grid, grid_width, grid_height, image_size, images, buttons, bg_color, x_where_grid_ends):
        self._surface = surface
        self._grid = grid
        self._grid_width = grid_width
        self._grid_height = grid_height
        self._image_size = image_size
        self._images = images
        self._buttons = buttons
        self._bg_color = bg_color
        self.x_where_grid_ends = x_where_grid_ends

    def render(self):
        self._surface.fill(self._bg_color)
        self.draw_grid()
        self.draw_side_buttons()
        pygame.display.flip()

    def draw_grid(self):
        for y in range(self._grid_height):
            for x in range(self._grid_width):
                square = self._grid[y][x]
                # every image is 100x100 pixels, so a drawn square should always be scaled from that size
                self._surface.blit(self._images[square],
                                   (x * self._image_size[0], y * self._image_size[1]))

    def draw_side_buttons(self):
        for button_index, button in enumerate(self._buttons):
            (self._surface.blit(button,
            (WINDOW_WIDTH - DEFAULT_SIDE_BUTTON_IMAGE_SIZE[0], button_index * DEFAULT_SIDE_BUTTON_IMAGE_SIZE[1])))