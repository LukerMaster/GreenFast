import PygameRenderer.pyrenderer as pr
from pygameloop import PygameLoop
from CircleGame.circlegame import CircleGame
import CircleGame.inputmanagers as kb


class Gameplay:
    def __init__(self):
        self.controller_manager = kb.KeyboardInputManager()
        self.program_loop = None
        self.game = None
        self.renderer = None
        self.renderer = pr.Renderer(1000, 1000)
        self.reset()

    def start(self):
        self.program_loop.loop()

    def reset(self):
        self.program_loop = PygameLoop()
        self.game = CircleGame()
        self.renderer.set_game(self.game)

        def update(dt):
            controls = self.controller_manager.get_controls()  # This can be replaced by any kind of AI controller
            if controls.esc:
                self.program_loop.is_on = False
            self.game.update(dt, controls)
            self.renderer.display()

        self.program_loop.update_fn = update