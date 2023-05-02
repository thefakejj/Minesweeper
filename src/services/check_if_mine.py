def square_is_mine(square_coordinates: tuple, field_grid: list):
    if check_square_content(square_coordinates, field_grid) == 1:
        return True
    else:
        return False

def check_square_content(square_coordinates: tuple, field_grid: list):
    return field_grid[square_coordinates[1]][square_coordinates[0]]

def nearby_mines(square_coordinates: tuple, field_grid: list):
    if square_is_mine(square_coordinates, field_grid):
        # corresponds to a mine
        return -1
    else:
        return count_nearby_mines(square_coordinates, field_grid)

def count_nearby_mines(square_coordinates: tuple, field_grid: list):
    mines = 0
    for i in range(square_coordinates[0]-1, square_coordinates[0]+2):
        for j in range(square_coordinates[1]-1, square_coordinates[1]+2):
            if i < 0 or j < 0 or i >= len(field_grid) or j >= len(field_grid):
                continue
            if field_grid[j][i] == 1:
                mines += 1
    return mines

    # how empty..?
    # maybe calculate squares around and bomb count, maybe even make list
    # of empty squares that are connected