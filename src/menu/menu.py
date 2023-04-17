import pygame_menu


class Menu:
    def __init__(self, minesweeper):
        self.minesweeper = minesweeper

    # ChatGPT was used to change this function, instead of calling the start_game function by typing self.minesweeper.start_game(), the function is simply referenced with self.minesweeper.start_game
    def menu(self):
        print("Moi:)")
        main_menu = pygame_menu.Menu(
            'Settings', 1280, 720, theme=pygame_menu.themes.THEME_BLUE)
        # Chatgpt | here the function is only referenced instead of called
        main_menu.add.button('Play', self.minesweeper.start_game)
        # Chatgpt | here the values of the selector are integers that can be used for the grid's size
        # this should be changed to return tuples like (8, 8) if different widths and heights of the field are introduced
        main_menu.add.selector(
            'Field size :', [('8x8', (8, 8)), ('16x16', (16, 16)), ('30x16', (32, 16))], onchange=self.minesweeper.set_minesweeper_size)

        main_menu.add.button('Quit', pygame_menu.events.EXIT)

        main_menu.mainloop(self.minesweeper.surface)