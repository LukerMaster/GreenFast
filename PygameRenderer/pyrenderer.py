import pygame
import CircleGame as cg


class Renderer:

    def __init__(self, size_x, size_y):
        if not pygame.display.get_init():
            pygame.display.init()
        self.screen = pygame.display.set_mode((size_x, size_y))

    def display(self, arena):
        self.screen.fill((128, 128, 128))

        pygame.draw.rect(self.screen, (20, 20, 80), pygame.Rect(0, 0, arena.playfield_size, arena.playfield_size), )

        pygame.draw.circle(self.screen, arena.player.color, arena.player.position[::-1], arena.player.radius)

        for enemy in arena.homing_enemies:
            pygame.draw.circle(self.screen, enemy.color, enemy.position[::-1], enemy.radius)
        for obstacle in arena.obstacles:
            pygame.draw.circle(self.screen, obstacle.color, obstacle.position[::-1], obstacle.radius)
        for win in arena.win_circles:
            pygame.draw.circle(self.screen, win.color, win.position[::-1], win.radius)

        pygame.display.flip()