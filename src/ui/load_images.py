import os
import pygame
from constants import DEFAULT_SIDE_BUTTON_IMAGE_SIZE

dirname = os.path.dirname(__file__)


class Images:
    """class that holds lists for images
    Attributes:
        image_size: image size after scaling
        images: list of tile images
        buttons: list of button images
    """

    def __init__(self, image_size: tuple):
        """creates object and loads images from the assets directory into lists

        Args:
            image_size (tuple): dimensions for tile images
        """
        self.image_size = image_size
        self.images = []
        self.buttons = []
        self.load_images()

    def load_images(self):
        """loads images into the images and buttons lists
        """
        for name in (["unrevealed_tile", "flag", "mine", "revealed_0", "revealed_1", "revealed_2", "revealed_3",
                      "revealed_4", "revealed_5", "revealed_6", "revealed_7", "revealed_8"]):
            image = pygame.image.load(
                os.path.join(dirname, "..", "assets", name + ".png"))
            image = pygame.transform.scale(image, self.image_size)
            self.images.append(image)

        for name in ["back_to_menu"]:
            image = pygame.image.load(
                os.path.join(dirname, "..", "assets", name + ".png"))
            image = pygame.transform.scale(
                image, DEFAULT_SIDE_BUTTON_IMAGE_SIZE)
            self.buttons.append(image)
