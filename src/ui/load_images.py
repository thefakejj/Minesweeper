import pygame
import os


dirname = os.path.dirname(__file__)


class Images:
    def __init__(self, image_size):
        self.image_size = image_size
        self.images = []
        self.load_images()

    def load_images(self):
        for name in ["unrevealed_tile", "flag", "mine", "revealed_0"]:
            image = pygame.image.load(
                os.path.join(dirname, "..", "assets", name + ".png"))
            image = pygame.transform.scale(image, self.image_size)
            self.images.append(image)

    def give_image(self, image_number):
        return self.images[image_number]
