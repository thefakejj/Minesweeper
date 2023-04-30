import unittest
from services.game import Minesweeper
from services.field import Field


class TestMinesweeper(unittest.TestCase):
    def setUp(self):
        self.minesweeper = Minesweeper()
        self.minesweeper.real_field = Field(self.minesweeper.grid_width, self.minesweeper.grid_height)

    def test_size_is_set_correctly(self):
        self.minesweeper.set_minesweeper_size("_", (10, 8))
        self.assertEqual(self.minesweeper.grid_width, 10)
        self.assertEqual(self.minesweeper.grid_height, 8)


    def test_first_click_has_happened_begins_false(self):
        self.assertEqual(self.minesweeper.first_click_has_happened, False)


    def test_start_game_makes_first_click_true(self):
        self.minesweeper.start_game((2, 4)) #needs parameters
        self.assertEqual(self.minesweeper.first_click_has_happened, True)

    def test_start_game_makes_changes_game_state(self):
        self.minesweeper.start_game((2, 4)) #needs parameters
        self.assertEqual(self.minesweeper.game_state, 2)

    def test_start_game_creates_field_without_mine_on_first_click_square(self):
        self.minesweeper.start_game((2, 4)) #needs parameters
        self.assertEqual(self.minesweeper.real_field.grid[4][2], 0)


    def test_game_state_default_correct(self):
        self.assertEqual(self.minesweeper.game_state, 0)

    def test_game_state_changes_correctly(self):
        self.minesweeper.change_game_state(1)
        self.assertEqual(self.minesweeper.game_state, 1)
