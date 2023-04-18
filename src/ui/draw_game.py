# import pygame


# # ui methods

# def draw_surface():

#     surface.fill(bg_color)
#     draw_grid()


# def draw_grid():
#     for y in range(minesweeper.grid_height):
#         for x in range(minesweeper.grid_width):
#             square = minesweeper.grid[y][x]
#             # every image is 100x100 pixels, so a drawn square should always be scaled from that size
#             surface.blit(minesweeper.images[square],
#                                 (x * minesweeper.get_scaled_image_size()[0], y * minesweeper.get_scaled_image_size()[1]))
