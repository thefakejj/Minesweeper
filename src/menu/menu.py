import pygame_menu
import constants


class Menu:
    """class for pygame menu
    """
    def __init__(self, go_to_game, set_minesweeper_size, surface):
        """initiates pygame menu

        Args:
            go_to_game (function): minesweeper object's function for going into the game
            set_minesweeper_size (function): sets grid width and height in minesweeper object
            surface (minesweeper object): surface on top which pygame menu can draw it's own menu
        """
        self.go_to_game = go_to_game
        self.set_minesweeper_size = set_minesweeper_size
        self.surface = surface

    # ChatGPT was used to change this function, instead of calling the start_game function by typing self.minesweeper.start_game(), the function is simply referenced with self.minesweeper.start_game
    def menu(self):
        """pygame menu's default state
        """
        main_menu = pygame_menu.Menu(
            'Settings', constants.WINDOW_WIDTH, constants.WINDOW_HEIGHT, theme=pygame_menu.themes.THEME_BLUE)
        # Chatgpt | here the function is only referenced instead of called
        main_menu.add.button('Play', self.go_to_game)
        # Chatgpt | here the values of the selector are integers that can be used for the grid's size
        # this should be changed to return tuples like (8, 8) if different widths and heights of the field are introduced
        main_menu.add.selector(
            'Field size :', [('8x8', (8, 8)), ('16x16', (16, 16)), ('24x16', (24, 16))], onchange=self.set_minesweeper_size)

        main_menu.add.button('Quit', pygame_menu.events.EXIT)

        main_menu.mainloop(self.surface)
