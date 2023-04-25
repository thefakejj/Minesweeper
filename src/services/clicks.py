class ClickChecker:
    def __init__(self, image_size, grid_width, grid_height, x_where_grid_starts, x_where_grid_ends):
        # self.event_button = event_button # 1 3

        self.image_size = image_size

        self.grid_width = grid_width
        self.grid_height = grid_height

        self.x_where_grid_starts = x_where_grid_starts
        self.x_where_grid_ends = x_where_grid_ends

    def square_click(self, event_button, x_coordinate, y_coordinate, window_height,
                    first_click_has_happened, start_game, grid):
        # this jungle of if-statements determines
        # whether or not the click is within grid's dimensions

        # when click is inside the grid
        if x_coordinate >= self.x_where_grid_starts and x_coordinate <= self.x_where_grid_ends:
            if y_coordinate >= 0 and y_coordinate <= window_height:

                (square_x, square_y) = self.which_square_was_clicked(
                    x_coordinate, y_coordinate)

                # upon left click
                if event_button == 1:
                    if grid.get_grid_square_from_coordinates(square_x, square_y) == 1:
                        return
                    if first_click_has_happened is False:
                        start_game((square_x, square_y))

                # upon right click
                if event_button == 3:
                    grid.update_ui_grid(
                        square_x, square_y, 2)

        # when click is outside the grid
        else:
            return

    def which_square_was_clicked(self, x_coordinate, y_coordinate):
        # y coordinates
        for height in range(self.grid_height):
            # grid will always start at y=0 and end at y = window_height
            if (y_coordinate >= 0+(height*self.image_size[1])
                    and y_coordinate <= 0+((height+1)*self.image_size[1])):
                square_y = height

        # x coordinates
        for width in range(self.grid_width):
            # x-coordinates are given from the scaling module
            if (x_coordinate >= self.x_where_grid_starts+(width*self.image_size[1])
                    and x_coordinate <= self.x_where_grid_starts+((width+1)*self.image_size[1])):
                square_x = width

        return (square_x, square_y)