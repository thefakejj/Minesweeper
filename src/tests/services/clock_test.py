import unittest
from services.clock import Clock

# tests use tickrates 10^n to make it easier to calculate milliseconds
class TestClock(unittest.TestCase):
    def setUp(self):
        self.clock = Clock()

        self.start_time = 0
        self.elapsed_time = 0
        self.stop_time = 0
        self.finish_time = 0

    def test_elapsed_time(self):
        self.clock.set_start_time()
        self.clock.tick(100)

        self.clock.set_elapsed_time()

        self.assertEqual(self.clock.get_elapsed_time_in_seconds(), "0.01")

        self.clock.reset_elapsed_time()

        self.assertEqual(self.clock.get_elapsed_time_in_seconds(), "0.00")

    def test_finish_time(self):
        self.clock.set_start_time()
        self.clock.tick(100)
        self.clock.set_stop_time()

        self.clock.set_finish_time()
        self.assertEqual(self.clock.get_finish_time_in_seconds(), "0.01")
