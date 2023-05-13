import pygame


class Clock:
    """class for pygame clock, which is used for keeping a framerate and timing runs
    """

    def __init__(self):
        """creates a pygame clock object
            sets all time attributes to 0 and updates as the program is running
        Attributes:
            _clock: pygame clock object
            _start_time: when run was started
            _elapsed_time: how long run has lasted
            _stop_time: when run was stopped
            _finish_time: how long the whole run lasted
            
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
        """sets the start time for the current run in ticks
        """
        self._start_time = self.get_ticks()

    def get_start_time(self):
        """gives the run's start time

        Returns:
            int: start time in ticks
        """
        return self._start_time

    def set_stop_time(self):
        """sets the stop time for the current run in ticks
        """
        self._stop_time = self.get_ticks()

    def get_stop_time(self):
        """gives the run's start time

        Returns:
            int: stop time in ticks
        """
        return self._stop_time

    def set_elapsed_time(self):
        """sets the elapsed time for the current run in milliseconds
        """
        self._elapsed_time = self.get_ticks() - self.get_start_time()

    def reset_elapsed_time(self):
        """resets the elapsed time, so that the next run starts at 0
        """
        self._elapsed_time = 0

    def get_elapsed_time_in_seconds(self):
        """Gives current elapsed time of the run. This is constantly called by renderer.

        Returns:
            str: elapsed time in seconds with a two decimal precision
        """
        return f'{(self._elapsed_time/1000.0):.2f}'

    def set_finish_time(self):
        """sets the finish time for the current run in milliseconds
        """
        self._finish_time = self.get_stop_time() - self.get_start_time()

    def get_finish_time_in_seconds(self):
        """Gives finish time of the run. This is called by minesweeper to insert time into leaderboard.

        Returns:
            str: finish time in seconds with a two decimal precision
        """
        return f'{(self._finish_time/1000.0):.2f}'
