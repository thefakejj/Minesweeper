from enums.mouse_enum import MouseEnum
from constants import WINDOW_HEIGHT, DEFAULT_BACK_TO_MENU_COORDINATES, DEFAULT_SIDE_BUTTON_IMAGE_SIZE
from services.check_if_mine import square_is_mine, nearby_mines

class MouseEvent:
    def __init__(self, minesweeper):
        # self.event_button = event_button # 1 3
        self.minesweeper = minesweeper

        self.image_size = self.minesweeper.image_size

        self.grid_width = self.minesweeper.grid_width
        self.grid_height = self.minesweeper.grid_height

        self.x_where_grid_starts = self.minesweeper.x_where_grid_starts
        self.x_where_grid_ends = self.minesweeper.x_where_grid_ends
        
        self.change_game_state = self.minesweeper.change_game_state
        

    def side_button_click(self, click_coordinates):
        if (click_coordinates[0] >= DEFAULT_BACK_TO_MENU_COORDINATES[0]
            and click_coordinates[0] <= DEFAULT_BACK_TO_MENU_COORDINATES[0]+DEFAULT_SIDE_BUTTON_IMAGE_SIZE[0]):

            if (click_coordinates[1] >= DEFAULT_BACK_TO_MENU_COORDINATES[1]
                and click_coordinates[1] <= DEFAULT_BACK_TO_MENU_COORDINATES[1] + DEFAULT_SIDE_BUTTON_IMAGE_SIZE[1]):
                self.minesweeper.change_game_state(0)

    def square_click(self, event_button, click_coordinates,
                     first_click_has_happened, start_game, grid, field_grid):
        # this jungle of if-statements determines
        # whether or not the click is within grid's dimensions

        # when click is inside the grid
        if (click_coordinates[0] >= self.x_where_grid_starts
            and click_coordinates[0] <= self.x_where_grid_ends):
            if click_coordinates[1] >= 0 and click_coordinates[1] <= WINDOW_HEIGHT:

                square_coordinates = self.which_square_was_clicked(click_coordinates)

                click_type = None

                if event_button == MouseEnum.RIGHT_CLICK:
                    click_type = "rightclick"
                    #grid.update_ui_grid(
                        #square_coordinates, click_type, square_is_mine(square_coordinates, field_grid))
                    
                if event_button == MouseEnum.LEFT_CLICK:
                    click_type = "leftclick"
                    if square_is_mine(square_coordinates, field_grid):
                        self.change_game_state(3)
                    if grid.get_square_content(square_coordinates) == 1:
                        return
                    
                    elif first_click_has_happened is False:
                        start_game(square_coordinates)
                    
                    
                
                # update and check if mine. if mine, change game state
                grid.update_ui_grid(square_coordinates, click_type, nearby_mines(square_coordinates, field_grid))
                

        # when click is outside the grid
        else:
            return

    def which_square_was_clicked(self, click_coordinates):
        # y coordinates
        for height in range(self.grid_height):
            # grid will always start at y=0 and end at y = WINDOW_HEIGHT
            if (click_coordinates[1] >= 0+(height*self.image_size[1])
                    and click_coordinates[1] <= 0+((height+1)*self.image_size[1])):
                square_y = height

        # x coordinates
        for width in range(self.grid_width):
            # x-coordinates are given from the scaling module
            if ((click_coordinates[0] >= self.x_where_grid_starts+(width*self.image_size[1]))
            and click_coordinates[0] <= self.x_where_grid_starts+((width+1)*self.image_size[1])):
                square_x = width

        return (square_x, square_y)

