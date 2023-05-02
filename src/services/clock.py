import pygame


class Clock:
    """class for pygame clock
    """

    def __init__(self):
        """creates a pygame clock object
        """
        self._clock = pygame.time.Clock()

    def tick(self, fps):
        """ticks the pygame clock once 

        Args:
            fps (int): the framerate of the game
        """
        self._clock.tick(fps)

    def get_ticks(self):
        """returns current ticks from the pygame clock

        Returns:
            int: time in milliseconds since pygame was initiated
        """
        return pygame.time.get_ticks()
