# from time import time
import sys
import pygame


from menu.menu import Menu

# from services.game import main_loop, event_checker
from services.field import Field
from services.clicks import ClickChecker
from services.clock import Clock

from ui.renderer import Renderer
from ui.ui_grid import UiGrid
from ui.scaling import Scaling
from ui.load_images import Images

# from repositories.leaderboard_repository import

import constants


class Minesweeper:
    def __init__(self):
        pygame.init()

        self.window_width = constants.WINDOW_WIDTH
        self.window_height = constants.WINDOW_HEIGHT

        # ChatGPT | since the menu selectors change the size of the grid,
        # having a default grid size is necessary for now
        # default grid size, should be set inside menu
        # from database_connection import get_database_connection
        self.grid_width, self.grid_height = (8, 8)  # default grid size

        self.bg_color = (255, 255, 255)

        # game logic stuff starts

        # this attribute is false until the player has clicked on a tile.
        # Once it's clicked, this attribute will be True.
        self.first_click_has_happened = False

        # game states: 0 = menu, 1 = in game but no first click,
        # 2 = in game and has clicked a square, 3 = game lost, 4 = won game
        self.game_state = 0

        self.x_where_grid_starts = 0
        self.x_where_grid_ends = 0

        # self.start_time = 0
        # self.elapsed_time = 0
        # self.stop_time = 0
        # self.finish_time = 0

        self._clock = Clock()

    # game logic methods

    # main loop, on when start_game is called

    def main_loop(self):
        while True:
            # if self.game_state == 0:
            #     pass
            # if self.game_state == 1:
            #     pass
            # if self.game_state == 2:
            #     pass
            # if self.game_state == 3:
            #     pass
            self.renderer.render()
            self.event_checker()
            pygame.display.flip()
            self._clock.tick(60)

    # events

    def event_checker(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                click_coordinates = (event.pos[0], event.pos[1])

                # if event.button == 3:
                #     flag

                self.click_checker.square_click(event.button, click_coordinates,
                                                self.window_height, self.first_click_has_happened,
                                                self.start_game, self.ui_grid)

            # if event.type == pygame.K_ESCAPE:
            #     pygame.quit()
            #     sys.exit()

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    # menu

    # ChatGPT | method to run the menu from an external module

    def run_menu(self):
        menu = Menu(self.go_to_game, self.set_minesweeper_size, self.surface)
        menu.menu()

    # Chatgpt | as the correct values are already in the selector widget,
    # we can simply use value[1] to get acces to the value
    # This function could potentially also be removed entirely,
    # if onchange=self.set_minesweeper_size is changed to onchange=value[1]
    def set_minesweeper_size(self, _, value):
        self.grid_width = value[0]
        self.grid_height = value[1]

    # game starts

    # ChatGPT | the main loop will only be run once the "Play" button is pressed in the menu

    def go_to_game(self):
        self.game_state = 1

        # while drawing the surface needs ui_grid,
        # ui_grid needs parameters from this class
        # ui_grid cannot be defined before this
        self.ui_grid = UiGrid(self.grid_width, self.grid_height)

        # scaling
        scaling = Scaling(
            self.window_height, constants.DEFAULT_IMAGE_SIZE, self.grid_width, self.grid_height)
        scaling.get_max_scale()
        self.image_size = scaling.get_scaled_image_size()

        self.x_where_grid_starts, self.x_where_grid_ends = scaling.get_grid_edge_x_coordinates()

        self.click_checker = ClickChecker(
                                        self.image_size, self.grid_width, self.grid_height,
                                        self.x_where_grid_starts, self.x_where_grid_ends)

        # images
        images = Images(self.image_size)

        # renderer defined outside of init so that class can be tested
        # otherwise surface would appear during tests
        self.renderer = Renderer(self.surface, self.ui_grid.grid, self.grid_width,
                                 self.grid_height, self.image_size, images.images, self.bg_color)
        self.main_loop()

    def start_game(self, square_coordinates: tuple):
        self.first_click_has_happened = True
        self.change_game_state(2)
        self.real_field = Field(self.grid_width, self.grid_height, square_coordinates)
        # self.set_start_time()

    def change_game_state(self, desired_game_state: int):
        self.game_state = int(desired_game_state)

    # time methods
    # no time methods work right now so they'll be commented out for the time being

    def set_start_time(self):
        pass
        # self.start_time = time()
        # # if self.game_state == 2:
        # #     self.start_time = time()
        # # else:
        # #     return

    def get_start_time(self):
        pass
        # return self.start_time

    # when game ends
    def set_stop_time(self):
        pass
        # self.stop_time = time()
        # if self.game_state == 4:
        #     self.stop_time = time()
        # else:
        #     return

    def get_stop_time(self):
        pass
        # return self.stop_time

    def set_elapsed_time(self):
        pass
        # self.elapsed_time = time() - self.start_time
        # if self.game_state == 2:
        #     self.elapsed_time = self.get_current_time() - self.get_start_time()
        # # can be used as in-game clock
        # else:
        #     return

    def get_elapsed_time(self):
        pass
        # return self.elapsed_time
