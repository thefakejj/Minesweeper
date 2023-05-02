import unittest
from services.check_if_mine import square_is_mine, check_square_content, nearby_mines, count_nearby_mines

class TestCheckIfMine(unittest.TestCase):
    def setUp(self):
        self.field = [
        [1, 0, 0, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1],
        [0, 1, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0, 0, 0, 0]
        ]

    def test_square_is_mine_if_mine(self):
        self.assertEqual(square_is_mine((6, 6), self.field), True)

    def test_check_square_content(self):
        self.assertEqual(check_square_content((6, 6), self.field), 1)
        self.assertEqual(check_square_content((7, 7), self.field), 0)

    def test_count_nearby_mines_returns_two(self):
        self.assertEqual(count_nearby_mines((6, 1), self.field), 2)

    def test_count_nearby_mines_returns_zero(self):
        self.assertEqual(count_nearby_mines((2, 1), self.field), 0)

    def test_count_works_at_edge(self):
        self.assertEqual(count_nearby_mines((7, 7), self.field), 1)

    def test_nearby_mines_returns_negative_one(self):
        self.assertEqual(nearby_mines((6, 6), self.field), -1)

    def test_nearby_mines_returns_mine_count(self):
        self.assertEqual(nearby_mines((5, 0), self.field), 2)
