import pygame_menu

class Menu:
    def __init__(self, minesweeper):
         self.minesweeper = minesweeper
    
    def set_minesweeper_size(self, value):
            if value == 1:
                return 8
            if value == 2:
                return 16

    def menu(self):
        print("Moi:)")
        main_menu = pygame_menu.Menu('Settings', 400, 300,
                        theme=pygame_menu.themes.THEME_BLUE)
        main_menu.add.button('Play', self.minesweeper.start_game())
        main_menu.add.selector('Field size :', [('8x8', 1), ('16x16', 2)], onchange=self.set_minesweeper_size)

        main_menu.add.button('Quit', pygame_menu.events.EXIT)

        main_menu.mainloop(self.minesweeper.surface)
        print(self.minesweeper.width)




