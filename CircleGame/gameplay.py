import PygameRenderer.pyrenderer as pr
from pygameloop import PygameLoop
from CircleGame.circlegame import CircleGame


class Gameplay:
    def __init__(self):
        self.program_loop = PygameLoop()
        self.game = CircleGame()
        self.renderer = pr.Renderer(self.game, 1000, 1000)

        def update(dt):
            self.game.update(dt)
            self.renderer.display()
            if self.game.exit_requested:
                self.program_loop.is_on = False

        self.program_loop.update_fn = update

    def start(self):
        self.program_loop.loop()
