import unittest
from services.game import Minesweeper


class TestMinesweeper(unittest.TestCase):
    def setUp(self):
        self.minesweeper = Minesweeper()
        # self.window_width = 1600
        # self.window_height = 900
        self.filler_arg_for_set_minesweeper_size = "_"
        self.wanted_dimensions = (10, 10)

        # self.grid_width = self.grid_size[0]
        # self.grid_height = self.grid_size[1]

        # self.scale = 1.5
        # self.default_image_size = (100, 100)
        # self.image_size = (100, 100)

        # self.x_where_grid_starts = 0
        # self.y_where_grid_starts = 0

        # self.x_where_grid_ends = 0
        # self.y_where_grid_ends = 0

        # self.first_click_has_happened = False

        # self.clock = pygame.time.Clock()

        # self.start_time = 0
        # self.stop_time = 0
        # self.current_time = 0
        # self.elapsed_time = self.current_time - self.start_time
        # self.finish_time = self.stop_time - self.start_time

    def test_scale_is_set_correctly(self):
        self.minesweeper.set_minesweeper_size(self.filler_arg_for_set_minesweeper_size, (8, 8))
        self.minesweeper.set_scale_to_max_possible()
        self.assertEqual(self.minesweeper.scale, 0.9)
