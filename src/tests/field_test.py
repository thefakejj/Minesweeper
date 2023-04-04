import unittest
from field import Field


class TestField(unittest.TestCase):
    def setUp(self):
        self.size = 8
        self.mines = 10
        self.field = Field(self.size)
    
    def test_grid_exists(self):
        self.assertNotEqual(self.field.grid, None)

    def test_str_is_correct(self):
        self.assertEqual(str(self.field), f"Field (scale={self.size}, mine count={self.mines})")

    def test_grid_correct_height(self):
        self.assertEqual(len(self.field.grid), self.size)

    def test_grid_correct_width(self):
        for row in self.field.grid:
            self.assertEqual(len(row), self.size)
