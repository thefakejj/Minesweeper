from enum import Enum


class GridEnum(Enum):
    """Assigns number values to strings that represent states of tiles in the Grid class

    Args:
        Enum (str): string which the enumerate represents

    Returns:
        str, int: enum
    """
    UNREVEALED_TILE = 0
    FLAG = 1
    MINE = 2
    REVEALED_0 = 3
    REVEALED_1 = 4
    REVEALED_2 = 5
    REVEALED_3 = 6
    REVEALED_4 = 7
    REVEALED_5 = 8
    REVEALED_6 = 9
    REVEALED_7 = 10
    REVEALED_8 = 11

    def __eq__(self, other):
        if isinstance(other, int):
            return self.value == other
        return self.value == other.value
