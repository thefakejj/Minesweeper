from ui.game import Minesweeper
from repositories.leaderboard_repository import Leaderboard

from constants import CORRECT_TABLES

leaderboard = Leaderboard()


if leaderboard.get_tables() == CORRECT_TABLES:
    minesweeper = Minesweeper()
else:
    print("First run this command in root directory: poetry run invoke build")
