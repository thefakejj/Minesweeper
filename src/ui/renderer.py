import pygame


class Renderer:
    def __init__(self, surface, grid, grid_width, grid_height, image_size, images, bg_color):
        self._surface = surface
        self._grid = grid
        self._grid_width = grid_width
        self._grid_height = grid_height
        self._image_size = image_size
        self._images = images
        self._bg_color = bg_color

    def render(self):
        self._surface.fill(self._bg_color)
        self.draw_grid()
        pygame.display.flip()

    def draw_grid(self):
        for y in range(self._grid_height):
            for x in range(self._grid_width):
                square = self._grid[y][x]
                # every image is 100x100 pixels, so a drawn square should always be scaled from that size
                self._surface.blit(self._images[square],
                                   (x * self._image_size[0], y * self._image_size[1]))
