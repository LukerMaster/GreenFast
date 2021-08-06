import PygameRenderer.pyrenderer as pr
from pygameloop import PygameLoop
from CircleGame.circlegame import CircleGame
import CircleGame.inputmanagers as kb


class Gameplay:
    def __init__(self):
        self.program_loop = PygameLoop()
        self.game = CircleGame()
        self.renderer = pr.Renderer(self.game, 1000, 1000)
        self.controller_manager = kb.KeyboardInputManager()

        def update(dt):
            controls = self.controller_manager.get_controls()  # This can be replaced by any kind of AI controller
            self.game.update(dt, controls)
            self.renderer.display()
            if self.game.exit_requested:
                self.program_loop.is_on = False

        self.program_loop.update_fn = update

    def start(self):
        self.program_loop.loop()
