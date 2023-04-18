import os
# time for timing a game of minesweeper, pygame's time for clock to reduce wasted computing power? I'll look into this
import time
import pygame
from menu.menu import Menu
from services.field import Field
# from services.game import main_loop, event_checker

dirname = os.path.dirname(__file__)


class Minesweeper:
    def __init__(self):
        pygame.init()

        # constructor beings with ui stuff

        # if the size of the grid is selected in the menu, the caption could be pygame.display.set_caption(f"Minesweeper {self.grid_width}x{self.grid_height}")
        # the previous is impossible because the menu is drawn over an object of the Minesweeper class
        pygame.display.set_caption("Minesweeper")

        self.window_width = 1600
        self.window_height = 900

        # ChatGPT | since the menu selectors change the size of the grid, having a default grid size is necessary for now
        # default grid size, should be set inside menufrom database_connection import get_database_connection
        self.grid_size = (8, 8)

        self.grid_width = self.grid_size[0]
        self.grid_height = self.grid_size[1]

        self.scale = 1.5  # default scale, i dont know how this should be implemented
        self.default_image_size = (100, 100)
        self.image_size = (100, 100)
        self.images = []

        self.x_where_grid_starts = 0
        # this will always be 0, as any grid will touch the top of the window
        self.y_where_grid_starts = 0

        self.x_where_grid_ends = 0
        self.y_where_grid_ends = 0

        self.surface = pygame.display.set_mode(
            (self.window_width, self.window_height))

        # currently trying to make a working game loop
        # setting a background color for the surface to test
        # maybe make it a private attribute?
        self.bg_color = (255, 255, 255)

        # game logic stuff starts

        # this attribute is false until the player has clicked on a tile. Once it's clicked, this attribute will be True.
        self.first_click_has_happened = False

        self.clock = pygame.time.Clock()

        # timer, begins once start_timer is called, ends once stop_timer is called. needs to be changed if pausing is introduced into the game.
        self.start_time = 0
        self.stop_time = 0
        self.current_time = self.time()
        # this will always display the elapsed time, if game hasnt started, the difference will be 0
        # displaying the elapsed time can work as an in-game clock, as it continuously updates
        self.elapsed_time = self.current_time - self.start_time
        self.finish_time = self.stop_time - self.start_time

        self.run_menu()

    # game logic methods

    def main_loop(self):
        while True:
            self.time()
            self.draw_surface()
            self.event_checker()
            pygame.display.flip()
            self.clock.tick(60)

    def event_checker(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                x_position = event.pos[0]
                y_position = event.pos[1]

                self.square_click(x_position, y_position)

            if event.type == pygame.K_ESCAPE:
                pygame.quit()
                exit()

            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

    def square_click(self, x_coordinate, y_coordinate):
        # this jungle of if-statements determines whether or not the click is within grid's dimensions
        if x_coordinate >= self.x_where_grid_starts and x_coordinate <= self.x_where_grid_ends:
            if y_coordinate >= self.y_where_grid_starts and y_coordinate <= self.y_where_grid_ends:
                pass
        else:
            return

        square_coordinates = self.which_square_was_clicked(
            x_coordinate, y_coordinate)

        if self.first_click_has_happened == False:

            self.start_game(square_coordinates)

    def which_square_was_clicked(self, x_coordinate, y_coordinate):
        for y in range(self.grid_height):
            if y_coordinate >= self.y_where_grid_starts+(y*self.get_scaled_image_size()[1]) and y_coordinate <= self.y_where_grid_starts+((y+1)*self.get_scaled_image_size()[1]):
                square_y = y

        for x in range(self.grid_width):
            if x_coordinate >= self.x_where_grid_starts+(x*self.get_scaled_image_size()[1]) and x_coordinate <= self.x_where_grid_starts+((x+1)*self.get_scaled_image_size()[1]):
                square_x = x

        # for x in range(self.grid_width):
        return (square_x, square_y)

    # ChatGPT | the main loop will only be run once the "Play" button is pressed in the menu

    def go_to_game(self):
        self.create_grid()
        self.set_scale_to_max_possible()
        self.load_images()
        self.main_loop()

    def start_game(self, square_coordinates: tuple):
        self.first_click_has_happened = True
        Field(self.grid_size, square_coordinates) # self.field = Field(self.grid_size, square_coordinates)
        self.start_timer()

    # ChatGPT | method to run the menu from an external module
    def run_menu(self):
        menu = Menu(self)
        menu.menu()

    def start_timer(self):
        self.start_time = time.time()

    def stop_timer(self):
        self.stop_time = time.time()

    def time(self):
        return time.time()

    # Chatgpt | as the correct values are already in the selector widget, we can simply use value[1] to get acces to the value
    # This function could potentially also be removed entirely, if onchange=self.set_minesweeper_size is changed to onchange=value[1]
    def set_minesweeper_size(self, _, value):
        self.grid_size = value
        self.grid_width = value[0]
        self.grid_height = value[1]

    # ui methods

    def draw_surface(self):

        self.surface.fill(self.bg_color)
        self.draw_grid()

    # 100*scale*grid_height<=720
    # scale*grid_height <= 7.2
    # scale <= 7.2/grid_height
    def set_scale_to_max_possible(self):
        self.scale = (self.window_height /
                      self.default_image_size[1])/self.grid_height

    def create_grid(self):
        self.set_scale_to_max_possible()
        self.grid = [[0]*self.grid_width for i in range(self.grid_height)]
        self.get_grid_edge_coordinates()

    def draw_grid(self):
        for y in range(self.grid_height):
            for x in range(self.grid_width):
                square = self.grid[y][x]
                # every image is 100x100 pixels, so a drawn square should always be scaled from that size
                self.surface.blit(self.images[square],
                                  (x * self.get_scaled_image_size()[0], y * self.get_scaled_image_size()[1]))

    def load_images(self):
        for name in ["unrevealed_tile", "mine", "flag"]:
            image = pygame.image.load(
                os.path.join(dirname, "..", "assets", name + ".png"))
            image = pygame.transform.scale(image, self.get_scaled_image_size())
            self.images.append(image)

    def get_scaled_image_size(self):
        return (self.scale*self.image_size[0], self.scale*self.image_size[1])

    def get_grid_edge_coordinates(self):
        self.x_where_grid_ends = self.get_scaled_image_size()[
            0]*self.grid_width
        self.y_where_grid_ends = self.get_scaled_image_size()[
            1]*self.grid_width
        return self.x_where_grid_ends, self.y_where_grid_ends
