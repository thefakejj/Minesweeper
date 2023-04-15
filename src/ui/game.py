import os
# time for timing a game of minesweeper, pygame's time for clock to reduce wasted computing power? I'll look into this
import time
import pygame
import pygame_menu

dirname = os.path.dirname(__file__)


class Minesweeper:
    def __init__(self):
        pygame.init()
        # if the size of the grid is selected in the menu, the caption could be pygame.display.set_caption(f"Minesweeper {scale}x{scale} or {horizontal}x{vertical}")
        # the previous is impossible because the menu is drawn over an object of the Minesweeper class
        pygame.display.set_caption("Minesweeper")

        self.width = 640
        self.height = 480

        self.surface = pygame.display.set_mode((self.width, self.height))
        
        self.clock = pygame.time.Clock()

        # currently trying to make a working game loop
        # setting a background color for the surface to test
        # maybe make it a private attribute?
        self.bg_color = (128, 128, 128)

        self.main_loop()
        self.menu()
    #     self.open_menu()

    # def open_menu(self):
    #     menu = pygame_menu.Menu('Settings', 400, 300,
    #                    theme=pygame_menu.themes.THEME_BLUE)
    #     menu.add.button('Play', self.start_game(self.set_minesweeper_size))
    #     menu.add.selector('Field size :', [('8x8', 1), ('16x16', 2)], onchange=self.set_minesweeper_size)

    #     menu.add.button('Quit', pygame_menu.events.EXIT)


    def main_loop(self):
        while True:
            self.draw_surface()
            self.event_checker()
            pygame.display.flip()
            self.clock.tick(60)

    def event_checker(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.x_position = event.pos[0]
                self.y_position = event.pos[1]
            
            if event.type == pygame.K_ESCAPE:
                pygame.quit()
                exit()

            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

    def draw_surface(self):

        self.surface.fill(self.bg_color)

    # def set_minesweeper_size(self, value, size):
    #     if value == 1:
    #         return 8
    #     if value == 2:
    #         return 16


    def set_minesweeper_size(self, value):
            if value == 1:
                return 8
            if value == 2:
                return 16

    def menu(self):
        menu = pygame_menu.Menu('Settings', 400, 300,
                        theme=pygame_menu.themes.THEME_BLUE)
        menu.add.button('Play', start_game())
        menu.add.selector('Field size :', [('8x8', 1), ('16x16', 2)], onchange=set_minesweeper_size)

        menu.add.button('Quit', pygame_menu.events.EXIT)

        menu.mainloop(self.surface)