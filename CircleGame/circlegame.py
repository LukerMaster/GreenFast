
from CircleGame.arena import Arena


class CircleGame:

    def __init__(self):
        self.arena = None

        self.points = 0
        self.peak_points = 0
        self.streak = 0

        self.lost_observers = []
        self.win_observers = []

        self._create_arena()

    def update(self, dt, controls):

        self.arena.update(dt, controls)

        if self.arena.is_win():
            self.set_points(self.points + 1)
            self._notify_win()
            self._create_arena()
        elif self.arena.is_lost():
            self.set_points(self.points - 1)
            self._notify_lost()
            self._create_arena()

    def set_points(self, points):

        if self.points < points:
            if self.streak < 0:
                self.streak = 1
            else:
                self.streak += 1

        if self.points > points:
            if self.streak > 0:
                self.streak = -1
            else:
                self.streak -= 1

        self.points = points
        if self.points < 0:
            self.points = 0
        if points > self.peak_points:
            self.peak_points = points

    def _create_arena(self):
        """Creates the game arena based on how many points the player has
        So the game becomes harder with more points"""
        self.arena = Arena((self.points // 2) + 3, self.points // 3, max(1, max(1, self.points) ** 0.1))

    def add_win_observer(self, observer):
        self.win_observers.append(observer)

    def add_lost_observer(self, observer):
        self.lost_observers.append(observer)

    def _notify_win(self):
        for ob in self.win_observers:
            ob()

    def _notify_lost(self):
        for ob in self.lost_observers:
            ob()
