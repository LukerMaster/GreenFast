import CircleGame.inputmanagers as kb

from CircleGame.arena import Arena


class CircleGame:
    points = 0
    exit_requested = False
    controller_manager = kb.KeyboardInputManager()

    def __init__(self):
        self.create_arena()

    def update(self, dt):
        controls = self.controller_manager.get_controls()
        self.arena.update(dt, controls)


        if self.arena.is_win():
            self.points += 1
            self.create_arena()
        elif self.arena.is_lost():
            self.points -= 1
            self.create_arena()

        if controls.esc:
            self.exit_requested = True

    def create_arena(self):
        print(f"Points: {self.points}")
        self.arena = Arena((self.points // 2) + 3, self.points // 3)