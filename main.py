import PygameRenderer.pyrenderer as pr
from pygameloop import PygameLoop
from CircleGame.circlegame import CircleGame


def main():

    program_loop = PygameLoop()
    game = CircleGame()
    renderer = pr.Renderer(game, 1000, 1000)

    def update(dt):
        game.update(dt)
        renderer.display()
        if game.exit_requested:
            program_loop.is_on = False

    program_loop.update_fn = update
    program_loop.loop()


if __name__ == '__main__':
    main()

