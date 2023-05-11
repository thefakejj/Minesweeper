from services.game import Minesweeper
import pygame


def run_minesweeper():
    """creates a minesweeper object and a surface for it, then runs the menu
    """
    minesweeper = Minesweeper()

    create_surface(minesweeper)

    minesweeper.run_menu()


def create_surface(minesweeper):
    pygame.display.set_caption("Minesweeper")
    minesweeper.surface = pygame.display.set_mode(
        (minesweeper.window_width, minesweeper.window_height))
