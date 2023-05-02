def square_is_mine(square_coordinates: tuple, field_grid: list):
    """checks if a square is mine in the backend

    Args:
        square_coordinates (tuple): x and y coordinates of the square
        field_grid (list): the field object's grid

    Returns:
        bool: returns true if square is mine, else returns false
    """
    if check_square_content(square_coordinates, field_grid) == 1:
        return True
    else:
        return False

def check_square_content(square_coordinates: tuple, field_grid: list):
    """checks field_grid's content of a specified square

    Args:
        square_coordinates (tuple): x and y coordinates of the square
        field_grid (list): the field object's grid

    Returns:
        int: 1 for mine, 0 for empty tile
    """
    return field_grid[square_coordinates[1]][square_coordinates[0]]

def nearby_mines(square_coordinates: tuple, field_grid: list):
    """checks if square is mine, else returns amount of surrounding mines

    Args:
        square_coordinates (tuple): x and y coordinates of the square
        field_grid (list): the field object's grid

    Returns:
        _type_: returns -1 for mine, otherwise returns amount of mines surrounding square
    """
    if square_is_mine(square_coordinates, field_grid):
        # corresponds to a mine
        return -1
    else:
        return count_nearby_mines(square_coordinates, field_grid)

def count_nearby_mines(square_coordinates: tuple, field_grid: list):
    """algorhithm for counting mines around the square

    Args:
        square_coordinates (tuple): x and y coordinates of the square
        field_grid (list): the field object's grid

    Returns:
        int: amount of mines surrounding the square
    """
    mines = 0
    for j in range(square_coordinates[1]-1, square_coordinates[1]+2):
        for i in range(square_coordinates[0]-1, square_coordinates[0]+2):
            if i < 0 or j < 0 or j >= len(field_grid) or i >= len(field_grid[0]):
                continue
            if field_grid[j][i] == 1:
                mines += 1
    return mines
