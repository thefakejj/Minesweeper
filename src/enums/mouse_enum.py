from enum import Enum

class MouseEnum(Enum):
    LEFT_CLICK = 1
    RIGHT_CLICK = 3

    # MIDDLE_CLICK = 2
    # SCROLL_UP = 4
    # SCROLL_DOWN = 5

    def __eq__(self, other):
        if isinstance(other, int):
            return self.value == other
        else:
            return self.value == other.value
