import unittest
from services.field import Field


class TestField(unittest.TestCase):
    def setUp(self):
        self.grid_width, self.grid_height = (8, 8)
        square_x = 5
        square_y = 3
        self.field = Field(self.grid_width, self.grid_height)
        self.field.create_random_field((square_x, square_y))

    def test_grid_correct_height(self):
        self.assertEqual(len(self.field.grid), self.grid_height)

    def test_grid_correct_width(self):
        for row in self.field.grid:
            self.assertEqual(len(row), self.grid_width)

    def test_mine_count_is_correct(self):
        mines = 0
        for row in range(8):
            for square in self.field.grid[row]:
                if square == 1:
                    mines += 1
        self.assertEqual(mines, 10)
