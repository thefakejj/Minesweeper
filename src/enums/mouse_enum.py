from enum import Enum


class MouseEnum(Enum):
    LEFT_CLICK = 1
    RIGHT_CLICK = 3

    def __eq__(self, other):
        if isinstance(other, int):
            return self.value == other
        return self.value == other.value
