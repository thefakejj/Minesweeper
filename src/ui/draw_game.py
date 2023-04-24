import pygame


class Draw:
    def __init__(self, surface, images, bg_color, grid):
        self.surface = surface
        self.images = images
        self.bg_color = bg_color
        self.grid = grid

    def draw_surface(self, surface):

        surface.fill(self.bg_color)
        draw_grid()

    def draw_grid(self, surface):
        for y in range(minesweeper.grid_height):
            for x in range(minesweeper.grid_width):
                square = minesweeper.grid[y][x]
                # every image is 100x100 pixels, so a drawn square should always be scaled from that size
                surface.blit(minesweeper.images[square],
                             (x * minesweeper.get_scaled_image_size()[0], y * minesweeper.get_scaled_image_size()[1]))
