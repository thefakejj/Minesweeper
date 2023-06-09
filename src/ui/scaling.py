class Scaling:
    """class for scaling the game according to resolution, assets' sizes and grid size
    Attributes:
        window_height: Minesweeper's window height
        default_image_size: default tile size from constants
        grid_width: minesweeper grid's width
        grid_height: minesweeper grid's height
        scale: tile image size based on window height and grid size
    """

    def __init__(self, window_height: int, default_image_size: tuple, grid_width: int, grid_height: int):
        """creates the scaling object and sets scale

        Args:
            window_height (int): Minesweeper's window height
            default_image_size (tuple): default tile images' dimensions
            grid_width (int): Minesweeper grid's width
            grid_height (int): Minesweeper grid's height
        """
        self.window_height = window_height
        self.default_image_size = default_image_size
        self.grid_width = grid_width
        self.grid_height = grid_height

        self.scale = self.get_max_scale()

    def get_max_scale(self):
        """sets the scale based on MATH

        Returns:
            float: scale as a float value
        """
        self.scale = (self.window_height /
                      self.default_image_size[1])/self.grid_height
        return self.scale

    def get_scaled_image_size(self):
        """scales the tile image size to largest size that fits

        Returns:
            tuple: image width and height
        """
        self.scale = self.get_max_scale()
        return (self.scale*self.default_image_size[0], self.scale*self.default_image_size[1])

    def get_grid_edge_x_coordinate(self):
        """gets x coordinates of visual grid after scaling

        Returns:
            tuple: grid's ending x coordinate
        """

        x_where_grid_ends = self.get_scaled_image_size()[0]*self.grid_width

        return x_where_grid_ends
