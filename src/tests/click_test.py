import unittest
from services.mouse_event import MouseEvent
from services.game import Minesweeper
from ui.scaling import Scaling


class TestMouseEvent(unittest.TestCase):
    def setUp(self):
        self.minesweeper = Minesweeper()
        scaling = Scaling(
            720, (100, 100), 8, 8)
        scaling.get_max_scale()
        # with an 8x8 grid and a surface with the dimensions 1280x720
        self.mouse_event = MouseEvent(self.minesweeper, (90, 90))

        self.minesweeper.change_game_state(2)
        self.minesweeper.first_click_has_happened = False
        self.ui_grid_no_mines = [[0]*8 for _ in range(8)]
        self.real_field_no_mines = [[0]*8 for _ in range(8)]

    def test_side_button_click_changes_game_state(self):
        self.mouse_event.side_button_click((1250, 30))
        self.assertEqual(self.minesweeper.game_state, 0)

    def test_side_button_click_changes_first_click(self):
        self.mouse_event.side_button_click((1250, 30))
        self.assertEqual(self.minesweeper.first_click_has_happened, False)

    def test_which_square_was_clicked_returns_correct_values(self):
        self.assertEqual(
            self.mouse_event.which_square_was_clicked((120, 120)), (1, 1))

    def test_square_click_changes_game_state(self):
        self.mouse_event.square_click(1, (120, 120), self.minesweeper.first_click_has_happened, self.minesweeper.start_game, self.ui_grid_no_mines, self.real_field_no_mines)
        self.assertEqual(self.minesweeper.game_state, 2)
