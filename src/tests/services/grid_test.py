import unittest
from services.grid import Grid
from ui.mouse_event import MouseEvent
from enums.grid_enum import GridEnum
from enums.mouse_enum import MouseEnum


class TestGrid(unittest.TestCase):
    def setUp(self):
        self.grid = Grid(8, 8)

        self.field_grid = [
            [1, 0, 0, 0, 1, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1],
            [0, 1, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0],
            [0, 1, 0, 0, 0, 0, 0, 0]
        ]

        self.empty_grid = [
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0]
        ]

        self.occupied_grid = [
            [1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 4]
        ]

        self.mouse_event = MouseEvent(
            (90, 90), 8, 8, 720, placeholder_change_game_state)

    def test_setup_grid_correct(self):
        self.assertEqual(self.grid.grid, self.empty_grid)

    def test_get_square_content(self):
        self.grid.grid = self.occupied_grid
        self.assertEqual(self.grid.get_square_content((0, 0)), 1)
        self.assertEqual(self.grid.get_square_content((1, 0)), 0)
        self.assertEqual(self.grid.get_square_content((7, 7)), 4)

    def test_set_square_content(self):
        self.assertEqual(self.grid.get_square_content((0, 0)), 0)
        self.grid.set_square_content((0, 0), GridEnum.REVEALED_0.value)
        self.assertEqual(self.grid.get_square_content((0, 0)), 3)

    def test_update_grid(self):
        self.assertEqual(self.grid.get_square_content((0, 0)), 0)

        # should have 0 revealed tiles at beginning
        self.assertEqual(self.grid.revealed_tiles, 0)

        # from unrevealed to flag
        self.grid.update_grid(
            (0, 0), MouseEnum.RIGHT_CLICK.value, self.field_grid)
        self.assertEqual(self.grid.get_square_content(
            (0, 0)), GridEnum.FLAG.value)

        # left clicking a flagged tile should do nothing
        self.grid.update_grid(
            (0, 0), MouseEnum.LEFT_CLICK.value, self.field_grid)
        self.assertEqual(self.grid.get_square_content(
            (0, 0)), GridEnum.FLAG.value)

        # from flag to unrevealed
        self.grid.update_grid(
            (0, 0), MouseEnum.RIGHT_CLICK.value, self.field_grid)
        self.assertEqual(self.grid.get_square_content(
            (0, 0)), GridEnum.UNREVEALED_TILE.value)

        # from unrevealed to 0 nearby
        self.grid.update_grid(
            (2, 1), MouseEnum.LEFT_CLICK.value, self.field_grid)
        self.assertEqual(self.grid.get_square_content(
            (2, 1)), GridEnum.REVEALED_0.value)

        # from unrevealed to 2 nearby
        self.grid.update_grid(
            (0, 1), MouseEnum.LEFT_CLICK.value, self.field_grid)
        self.assertEqual(self.grid.get_square_content(
            (0, 1)), GridEnum.REVEALED_2.value)

        # flagging revealed tile should do nothing
        self.grid.update_grid(
            (0, 1), MouseEnum.RIGHT_CLICK.value, self.field_grid)
        self.assertEqual(self.grid.get_square_content(
            (0, 1)), GridEnum.REVEALED_2.value)

        # revealing mine should set content to 2
        self.grid.update_grid(
            (0, 0), MouseEnum.LEFT_CLICK.value, self.field_grid)
        self.assertEqual(self.grid.get_square_content(
            (0, 0)), GridEnum.MINE.value)

    def test_check_if_enough_squares_flipped(self):
        # at the beginning flipped squares = 0
        # this should only return true, if flipped squares is equal or greater than 54
        self.assertEqual(self.grid.check_if_enough_squares_flipped(), False)
        self.grid.revealed_tiles = 53

        self.assertEqual(self.grid.check_if_enough_squares_flipped(), False)
        self.grid.revealed_tiles = 54

        self.assertEqual(self.grid.check_if_enough_squares_flipped(), True)
        self.grid.revealed_tiles = 55

        self.assertEqual(self.grid.check_if_enough_squares_flipped(), True)

    def test_count_nearby_mines(self):
        # on top of a mine
        self.assertEqual(self.grid.count_nearby_mines(
            (0, 0), self.field_grid), -1)

        # can return 0
        self.assertEqual(self.grid.count_nearby_mines(
            (2, 1), self.field_grid), 0)

        # can return other
        self.assertEqual(self.grid.count_nearby_mines(
            (0, 1), self.field_grid), 2)

    def test_mouse_event_revealing_mine_reveals_grid(self):

        self.assertEqual(self.count_unrevealed_tiles(self.grid.grid), 64)

        # mouse event flags a tile and opens a tile with mines near it
        self.mouse_event.square_click(MouseEnum.LEFT_CLICK.value, (150, 40),
                                      True, placeholder_start_game, self.grid, self.field_grid)

        self.mouse_event.square_click(MouseEnum.RIGHT_CLICK.value, (200, 40),
                                      True, placeholder_start_game, self.grid, self.field_grid)

        # when mouse_event opens mine tile, the grid reveal every tile
        # and be left with 0 unrevealed tiles
        # simulated click is somewhere within the first square
        self.mouse_event.square_click(MouseEnum.LEFT_CLICK.value, (40, 40),
                                      True, placeholder_start_game, self.grid, self.field_grid)

        # the amount of revealed files should now be 0
        self.assertEqual(self.count_unrevealed_tiles(self.grid.grid), 0)

    def count_unrevealed_tiles(self, grid):
        unrevealed = 0
        for row_index, _ in enumerate(grid):
            for _, square in enumerate(grid[row_index]):
                if square == GridEnum.UNREVEALED_TILE.value:
                    unrevealed += 1
        return unrevealed

# some functions need to be inserted into mouse_event and its methods,
# although they are unnecessary for the tests


def placeholder_change_game_state(state):
    pass


def placeholder_start_game():
    pass
