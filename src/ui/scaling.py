import pygame


class Scaling:
    def __init__(self, window_height, default_image_size, grid_width, grid_height):
        self.window_height = window_height
        self.default_image_size = default_image_size
        self.grid_width = grid_width
        self.grid_height = grid_height

        self.scale = self.get_max_scale()

    def get_max_scale(self):
        self.scale = (self.window_height /
                      self.default_image_size[1])/self.grid_height
        return self.scale

    def get_scaled_image_size(self):
        self.scale = self.get_max_scale()
        return (self.scale*self.default_image_size[0], self.scale*self.default_image_size[1])

    def get_grid_edge_x_coordinates(self):
        # this could be mathematically determined in the future so that the grid is centered or something of the sort
        x_where_grid_starts = 0

        x_where_grid_ends = self.get_scaled_image_size()[0]*self.grid_width

        return x_where_grid_starts, x_where_grid_ends
