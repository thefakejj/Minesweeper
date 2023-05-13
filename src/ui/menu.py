import pygame_menu
import constants

class Menu:
    """class for pygame menu
    """

    def __init__(self, go_to_game, set_minesweeper_size, surface, set_player_name, player_name: str, go_to_leaderboard):
        """initiates the pygame menu

        Args:
            go_to_game (function): Minesweeper's go_to_game function
            set_minesweeper_size (function): Minesweeper's set_minesweeper_size function
            surface (object): Minesweeper's surface object
            set_player_name (function): Minesweeper's set_player_name function
            player_name (str): Minesweeper's current player name
            go_to_leaderboard (function): Minesweeper's go_to_leaderboard function
        """

        self.go_to_game = go_to_game
        self.set_minesweeper_size = set_minesweeper_size
        self.surface = surface
        self.set_player_name = set_player_name
        self.player_name = player_name
        self.go_to_leaderboard = go_to_leaderboard


    # ChatGPT was used to change this function, instead of calling the start_game function by typing self.minesweeper.start_game(), the function is simply referenced with self.minesweeper.start_game
    def menu(self):
        """Adds all the buttons to menu and runs it
        """
        main_menu = pygame_menu.Menu(
            'Settings', constants.WINDOW_WIDTH, constants.WINDOW_HEIGHT, theme=pygame_menu.themes.THEME_BLUE)
        main_menu.add.text_input(
            'Name: ', default=self.player_name, maxchar=20, onchange=self.set_player_name)
        # Chatgpt | here the function is only referenced instead of called
        main_menu.add.button('Play', self.go_to_game)
        # Chatgpt | here the values of the selector are integers that can be used for the grid's size
        # this should be changed to return tuples like (8, 8) if different widths and heights of the field are introduced
        main_menu.add.selector(
            'Field size :', [('8x8', (8, 8)), ('16x16', (16, 16)), ('24x16', (24, 16))], onchange=self.set_minesweeper_size)
        main_menu.add.button('Leaderboard', self.go_to_leaderboard)

        main_menu.add.button('Quit', pygame_menu.events.EXIT)

        main_menu.mainloop(self.surface)
