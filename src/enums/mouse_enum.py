from enum import Enum


class MouseEnum(Enum):
    """Assigns number values to strings that represent pygame's event.button

    Args:
        Enum (str): string which the enumerate represents

    Returns:
        str, int: enum
    """
    LEFT_CLICK = 1
    RIGHT_CLICK = 3

    def __eq__(self, other):
        if isinstance(other, int):
            return self.value == other
        return self.value == other.value
