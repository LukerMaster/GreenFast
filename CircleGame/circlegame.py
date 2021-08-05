import CircleGame.inputmanagers as kb

from CircleGame.arena import Arena


class CircleGame:
    points = 0
    controller_manager = kb.KeyboardInputManager()

    def __init__(self):
        self.create_arena()

    def update(self, dt):
        self.arena.update(dt, self.controller_manager.get_controls())

        if self.arena.is_win():
            self.points += 1
            self.create_arena()
        elif self.arena.is_lost():
            self.points -= 1
            self.create_arena()

    def create_arena(self):
        print(f"Points: {self.points}")
        self.arena = Arena((self.points // 2) + 3, self.points // 3)