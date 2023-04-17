import os
# time for timing a game of minesweeper, pygame's time for clock to reduce wasted computing power? I'll look into this
import time
import pygame
from menu.menu import Menu
#from services.game import main_loop, event_checker

dirname = os.path.dirname(__file__)


class Minesweeper:
    def __init__(self):
        pygame.init()
        # if the size of the grid is selected in the menu, the caption could be pygame.display.set_caption(f"Minesweeper {scale}x{scale} or {horizontal}x{vertical}")
        # the previous is impossible because the menu is drawn over an object of the Minesweeper class
        pygame.display.set_caption("Minesweeper")

        self.width = 1280
        self.height = 720

        # ChatGPT | since the menu selectors change the size of the grid, having a default grid size is necessary for now
        self.grid_size = 16  # default grid size | later self.grid_size = (16, 16)

        self.grid_width = 16 # self.grid_width = self.grid_size[0]
        self.grid_height = 16 # self.grid_height = self.grid_size[1]
        

        self.surface = pygame.display.set_mode((self.width, self.height))

        self.clock = pygame.time.Clock()


        # timer, begins once start_timer is called, ends once stop_timer is called. needs to be changed if pausing is introduced into the game.
        self.start_time = 0
        self.stop_time = 0
        self.current_time = self.time()
        # this will always display the elapsed time, if game hasnt started, the difference will be 0
        # displaying the elapsed time can work as an in-game clock, as it continuously updates
        self.elapsed_time = self.current_time - self.start_time
        self.finish_time = self.stop_time - self.start_time


        # currently trying to make a working game loop
        # setting a background color for the surface to test
        # maybe make it a private attribute?
        self.bg_color = (128, 128, 128)

        self.run_menu()

        # self.main_loop()

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


    # ChatGPT | the main loop will only be run once the "Play" button is pressed in the menu
    def start_game(self):
        self.start_timer()
        self.main_loop()
        print("kukkuu, start_game funktiota just käytettiin!")

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
