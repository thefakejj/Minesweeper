import unittest
from repositories.leaderboard_repository import Leaderboard

class TestLeaderboardRepository(unittest.TestCase):
    def setUp(self):
        self.leaderboard = Leaderboard()
        self.leaderboard.delete_all()
        self.grid_sizes = [(8, 8), (16, 16), (24, 16)]

    def test_insert_works(self):
        for grid_size in self.grid_sizes:
            result = self.leaderboard.get_all(grid_size)
            self.assertEqual(len(result), 0)

            self.leaderboard.insert_time(grid_size, "Player", 113.76)
            result = self.leaderboard.get_all(grid_size)
            self.assertEqual(len(result), 1)

            self.assertEqual(result[0][1], "Player")
            self.assertEqual(result[0][2], 113.76)

    def test_query_filters_work(self):
        for grid_size in self.grid_sizes:
            self.leaderboard.insert_time(grid_size, "Player", 113.76)

            for i in range(10):
                if i < 5:
                    self.leaderboard.insert_time(grid_size, "Player", 146.22)
                else:
                    self.leaderboard.insert_time(grid_size, "Player", 177.05)

            result = self.leaderboard.grid_leaderboard(grid_size)
            print(result)
            # length should be 10 because of limit
            self.assertEqual(len(result), 10)

            # scores should be in order by time
            self.assertEqual(result[0][1], 113.76)
            self.assertEqual(result[3][1], 146.22)
            self.assertEqual(result[8][1], 177.05)
