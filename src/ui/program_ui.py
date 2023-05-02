from services.game import Minesweeper
from menu.menu import Menu
import pygame


def run_minesweeper():
    """creates a minesweeper object and a surface for it, then runs the menu
    """
    minesweeper = Minesweeper()

    create_surface(minesweeper)

    minesweeper.run_menu()


def create_surface(minesweeper):
    # if the size of the grid is selected in the menu, the caption could be pygame.display.set_caption(f"Minesweeper {self.grid_width}x{self.grid_height}")
    # the previous is impossible because the menu is drawn over an object of the Minesweeper class
    pygame.display.set_caption("Minesweeper")
    minesweeper.surface = pygame.display.set_mode(
        (minesweeper.window_width, minesweeper.window_height))
