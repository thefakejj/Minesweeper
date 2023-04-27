import unittest
from services.clicks import ClickChecker

class TestField(unittest.TestCase):
    def setUp(self):
        # lets set up a ClickChecker object that would be created
        # with an 8x8 grid and a surface with the dimensions 1280x720
        self.click_checker = ClickChecker((90, 90), 8, 8, 0, 720)
    

    def test_which_square_was_clicked_returns_correct_values(self):
        self.assertEqual(self.click_checker.which_square_was_clicked((120, 120)), (1, 1))
        