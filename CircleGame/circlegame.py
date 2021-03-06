import CircleGame.inputmanagers as kb

from CircleGame.arena import Arena


class CircleGame:
    points = 0
    peak_points = 0
    streak = 0
    exit_requested = False
    controller_manager = kb.KeyboardInputManager()

    lost_observers = []
    win_observers = []

    def __init__(self):
        self.arena = None
        self._create_arena()

    def update(self, dt):
        controls = self.controller_manager.get_controls()  # This can be replaced by any kind of AI controller

        self.arena.update(dt, controls)

        if self.arena.is_win():
            self.set_points(self.points + 1)
            self._notify_win()
            self._create_arena()
        elif self.arena.is_lost():
            self.set_points(self.points - 1)
            self._notify_lost()
            self._create_arena()

        if controls.esc:
            self.exit_requested = True

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