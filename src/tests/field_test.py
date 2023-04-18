import unittest
from services.field import Field


class TestField(unittest.TestCase):
    def setUp(self):
        self.size = (8, 8)
        self.height = self.size[1]
        self.width = self.size[0]
        self.first_click_coordinates = (150, 150)
        self.field = Field(self.size, self.first_click_coordinates)

    def test_grid_exists(self):
        self.assertNotEqual(self.field.grid, None)

    def test_str_is_correct(self):
        self.assertEqual(
            str(self.field), f"Field (size=8x8, , mine count=10)")

    def test_grid_correct_height(self):
        self.assertEqual(len(self.field.grid), self.height)

    def test_grid_correct_width(self):
        for row in self.field.grid:
            self.assertEqual(len(row), self.width)
