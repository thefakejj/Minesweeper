import unittest
from services.mouse_event import MouseEvent
from services.game import Minesweeper
from ui.scaling import Scaling

class TestField(unittest.TestCase):
    def setUp(self):
        self.minesweeper = Minesweeper()
        scaling = Scaling(
            720, (100, 100), 8, 8)
        scaling.get_max_scale()
        self.minesweeper.image_size = scaling.get_scaled_image_size()
        # lets set up a ClickChecker object that would be created
        # with an 8x8 grid and a surface with the dimensions 1280x720
        # self.mouse_event = MouseEvent((90, 90), 8, 8, 0, 720)
        self.mouse_event = MouseEvent(self.minesweeper)
    

    def test_which_square_was_clicked_returns_correct_values(self):
        self.assertEqual(self.mouse_event.which_square_was_clicked((120, 120)), (1, 1))
        