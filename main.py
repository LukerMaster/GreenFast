import PygameRenderer.pyrenderer as pr
from pygameloop import PygameLoop
from CircleGame.circlegame import CircleGame

def main():


    game_engine = PygameLoop()
    game = CircleGame()
    renderer = pr.Renderer(1000, 1000)



    def update(dt):
        game.update(dt)
        renderer.display(game.arena)

    game_engine.update_fn = update
    game_engine.loop()

if __name__ == '__main__':
    main()

