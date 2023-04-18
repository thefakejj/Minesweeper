from services.game import Minesweeper
from menu.menu import Menu
import pygame


def run_minesweeper():
    minesweeper = Minesweeper()

    # if the size of the grid is selected in the menu, the caption could be pygame.display.set_caption(f"Minesweeper {self.grid_width}x{self.grid_height}")
    # the previous is impossible because the menu is drawn over an object of the Minesweeper class
    pygame.display.set_caption("Minesweeper")
    minesweeper.surface = pygame.display.set_mode(
        (minesweeper.window_width, minesweeper.window_height))

    # currently trying to make a working game loop
    # setting a background color for the surface to test
    # maybe make it a private attribute?
    minesweeper.bg_color = (255, 255, 255)
    minesweeper.run_menu()
