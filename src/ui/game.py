#import os
import pygame

class Minesweeper:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Minesweeper") #if the size of the grid is selected in the menu, the caption could be pygame.display.set_caption(f"Minesweeper {scale}x{scale} or {horizontal}x{vertical}")



        self.width = 640
        self.height = 480


        pygame.display.set_mode((self.width, self.height))

        self.loop()

    


    def loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            pygame.display.update()