def square_is_mine(square_coordinates: tuple, field_grid: list):
    if check_square_content(square_coordinates, field_grid) == 1:
        return True
    else:
        return False

def check_square_content(square_coordinates: tuple, field_grid: list):
    return field_grid[square_coordinates[1]][square_coordinates[0]]


def square_is_empty(square_coordinates: tuple, field_grid: list):
    pass
    # how empty..?
    # maybe calculate squares around and bomb count, maybe even make list
    # of empty squares that are connected
