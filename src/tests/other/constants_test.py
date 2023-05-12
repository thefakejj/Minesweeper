import unittest
import constants

# these tests mainly exist because the constants get played around with in development


class TestConstants(unittest.TestCase):
    def setUp(self):
        pass

    def test_constants(self):
        self.assertEqual(constants.WINDOW_WIDTH, 1280)
        self.assertEqual(constants.WINDOW_HEIGHT, 720)
        self.assertEqual(constants.DEFAULT_IMAGE_SIZE, (100, 100))
        self.assertEqual(constants.DEFAULT_SIDE_BUTTON_IMAGE_SIZE, (200, 100))
        self.assertEqual(constants.DEFAULT_BACK_TO_MENU_COORDINATES, (1080, 0))
        self.assertEqual(constants.LEADERBOARD_SIZE, (700, 700))
        self.assertEqual(constants.LEADERBOARD_ROW_SIZE, (700, 60))
        self.assertEqual(constants.LEADERBOARD_NAME_CELL_SIZE, (500, 60))
        self.assertEqual(constants.LEADERBOARD_TIME_CELL_SIZE, (200, 60))
