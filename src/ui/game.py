import sys
import pygame

from menu.menu import Menu

# from services.game import main_loop, event_checker
from services.field import Field
from services.clock import Clock
from services.grid import Grid

from ui.mouse_event import MouseEvent
from ui.renderer import Renderer
from ui.scaling import Scaling
from ui.load_images import Images

from repositories.leaderboard_repository import Leaderboard

import constants


class Minesweeper:
    """Class that creates a minesweeper object, around which the game is built 
    Attributes:
        window_width, window_height: dimensions of the window set in constants
        grid_width, grid_height: default dimensions for the minesweeper grid
        bg_color: default background color
        first_click_has_happened: sets default value for if the player has clicked a tile open
        game_state: default game state, equates to being in menu
        x_where_grid_starts, x_where_grid_ends: default values for grid dimensions in pixels
        clock: creates a pygame clock object from external module

    """

    def __init__(self):
        """Class constructor that creates a new minesweeper object
        """

        pygame.init()

        self.window_width = constants.WINDOW_WIDTH
        self.window_height = constants.WINDOW_HEIGHT

        # ChatGPT | since the menu selectors change the size of the grid,
        # having a default grid size is necessary for now
        # default grid size, should be set inside menu
        self.grid_width, self.grid_height = (8, 8)  # default grid size

        self.bg_color = (128, 255, 128)

        self.player_name = ""

        # this attribute is false until the player has clicked on a tile.
        # Once it's clicked, this attribute will be True.
        self.first_click_has_happened = False

        # game states: 0 = menu, 1 = in game but no first click,
        # 2 = in game and has clicked a square, 3 = game lost, 4 = won game, 5 = leaderboard
        self.game_state = 0

        self.x_where_grid_starts = 0
        self.x_where_grid_ends = 0

        self.clock = Clock()

        self.leaderboard = Leaderboard()
        pygame.display.set_caption("Minesweeper")
        self.surface = pygame.display.set_mode(
            (constants.WINDOW_WIDTH, constants.WINDOW_HEIGHT))

        self.run_menu()

    # main loop, on when start_game is called

    def main_loop(self):
        """The loop of the game once "play" has been clicked
        """
        while True:
            if self.game_state == 0:
                self.run_menu()
            if self.game_state == 2:
                self.clock.set_elapsed_time()
                if self.grid.check_if_enough_squares_flipped():
                    self.change_game_state(4)
            if self.game_state == 3:
                pass
            if self.game_state == 5:
                pass
            self.renderer.render()
            self.event_checker()
            pygame.display.flip()
            self.clock.tick(60)

    # events

    def event_checker(self):
        """checks events for mouse clicks and some keypresses
        """
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                click_coordinates = (event.pos[0], event.pos[1])
                if 1 <= self.game_state <= 2:
                    self.mouse_event.square_click(event.button, click_coordinates,
                                                  self.first_click_has_happened,
                                                  self.start_game, self.grid,
                                                  self.real_field.grid)

                if event.button == 1:
                    self.mouse_event.side_button_click(click_coordinates)

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    # menu

    # ChatGPT | method to run the menu from an external module

    def run_menu(self):
        """runs pygame menu
        """
        menu = Menu(self.go_to_game, self.set_minesweeper_size, self.surface,
                    self.set_player_name, self.player_name, self.go_to_leaderboard)
        menu.menu()

    # Chatgpt | as the correct values are already in the selector widget,
    # we can simply use value[1] to get acces to the value
    # This function could potentially also be removed entirely,
    # if onchange=self.set_minesweeper_size is changed to onchange=value[1]
    def set_minesweeper_size(self, *args):
        """changes grid width and grid height of the minesweeper object
        Args:
            args[-1] is value from pygame menu.
        """
        value = args[-1]
        self.grid_width = value[0]
        self.grid_height = value[1]

    def set_player_name(self, *args):
        name = str(args[-1])
        self.player_name = name.strip()

    # game starts

    # ChatGPT | the main loop will only be run once the "Play" button is pressed in the menu

    def go_to_game(self):
        """goes into the game loop after creating and scaling UI, creating a field in the backend
        """
        if self.player_name == "":
            self.run_menu()

        self.change_game_state(1)
        self.change_view()

    def go_to_leaderboard(self):

        self.change_game_state(5)
        self.change_view()

    def change_view(self):
        # we create a field which is the grid in the backend
        # this is empty for now, and will be generated once first click occurs

        self.real_field = Field(self.grid_width, self.grid_height)

        # while drawing the surface needs grid,
        # grid needs parameters from this class
        # grid cannot be defined before this
        self.grid = Grid(self.grid_width, self.grid_height)

        # scaling
        scaling = Scaling(
            self.window_height, constants.DEFAULT_IMAGE_SIZE, self.grid_width, self.grid_height)
        scaling.get_max_scale()

        self.x_where_grid_starts, self.x_where_grid_ends = scaling.get_grid_edge_x_coordinates()

        # images
        image_size = scaling.get_scaled_image_size()
        images = Images(image_size)
        self.mouse_event = MouseEvent(self, image_size)

        # renderer defined outside of init so that class can be tested
        # otherwise surface would appear during tests

        self.renderer = Renderer(
            self, images.images, images.buttons, image_size)
        self.main_loop()

    def start_game(self, square_coordinates: tuple):
        """once the user has opened the first tile, the game saves this infomation 
            and creates a field in the backend

        Args:
            square_coordinates (tuple): x and y coordinates of the first click
        """
        self.first_click_has_happened = True
        self.change_game_state(2)
        self.real_field.create_random_field(square_coordinates)
        self.clock.set_start_time()

    def change_game_state(self, desired_game_state: int):
        """changes the game state and does necessary function calls
            game states: 0 = menu, 1 = in game but no first click,
            2 = in game and has clicked a square, 3 = game lost, 4 = won game

        Args:
            desired_game_state (int): the game state that the game is moving into
        """
        if desired_game_state == 0:
            self.set_minesweeper_size((8, 8))

        if desired_game_state == 1:
            self.first_click_has_happened = False
            self.clock.reset_elapsed_time()

        if desired_game_state == 2:
            self.clock.set_start_time()

        if desired_game_state == 3:
            self.clock.set_stop_time()
            self.mouse_event.reveal_grid(self.grid, self.real_field.grid)

        if desired_game_state == 4:
            self.clock.set_stop_time()
            self.clock.set_finish_time()
            self.mouse_event.reveal_grid(self.grid, self.real_field.grid)
            self.leaderboard.insert_time(
                (self.grid_width, self.grid_height),
                self.player_name,
                self.clock.get_finish_time_in_seconds())

        if desired_game_state == 5:
            pass

        self.game_state = int(desired_game_state)
