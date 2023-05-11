import pygame


class Clock:
    """class for pygame clock
    """

    def __init__(self):
        """creates a pygame clock object
        """
        self._clock = pygame.time.Clock()

        self._start_time = 0
        self._elapsed_time = 0
        self._stop_time = 0
        self._finish_time = 0

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

    def set_start_time(self):
        self._start_time = self.get_ticks()

    def get_start_time(self):
        return self._start_time

    def set_stop_time(self):
        self._stop_time = self.get_ticks()

    def get_stop_time(self):
        return self._stop_time

    def set_elapsed_time(self):
        self._elapsed_time = self.get_ticks() - self.get_start_time()

    def get_elapsed_time_in_seconds(self):
        return f'{(self._elapsed_time/1000.0):.2f}'

    def set_finish_time(self):
        self._finish_time = self.get_stop_time() - self.get_start_time()

    def get_finish_time_in_seconds(self):
        return f'{(self._finish_time/1000.0):.2f}'