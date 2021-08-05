import random, queue

import pygame
import CircleGame as cg


class Renderer:

    def __init__(self, game, size_x, size_y):
        if not pygame.display.get_init():
            pygame.display.init()
        self.screen = pygame.display.set_mode((size_x, size_y))
        self.canvas = None
        if not pygame.font.get_init():
            pygame.font.init()

        if not pygame.mixer.get_init():
            pygame.mixer.init()

        self.myfont = pygame.font.SysFont('Arial', 30)
        self.game = game

        self.win_sound = pygame.mixer.Sound("PygameRenderer/sounds/win.ogg")
        self.lose_sound = pygame.mixer.Sound("PygameRenderer/sounds/lost.ogg")
        pygame.mixer.music.load("PygameRenderer/sounds/literal_earrape.ogg")
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer.music.play(loops=-1)

        self.game.add_win_observer(lambda: self.win_sound.play())
        self.game.add_lost_observer(lambda: self.lose_sound.play())

        self.time = pygame.time.get_ticks()
        self.color = (20, 20, 80)

        self.previous_player_pos = queue.Queue()
        for i in range(40):
            self.previous_player_pos.put(self.game.arena.player.position)
        self.trail_color = (0, 140, 200)


    def display(self):
        self.screen.fill((128, 128, 128))
        self.canvas = pygame.Surface(self.game.arena.playfield_size)

        if pygame.time.get_ticks() - self.time > 228:
            self.time = pygame.time.get_ticks()
            self.color = (random.randint(0, 90), random.randint(0, 90), random.randint(0, 90))

        # Prepare points
        points_surface = self.myfont.render(f"Points: {str(self.game.points)}", False, (230, 230, 240, 150))
        max_points_surface = self.myfont.render(f"Max: {str(self.game.peak_points)}", False, (160, 160, 180, 100))

        # Draw background
        pygame.draw.rect(self.screen, self.color, pygame.Rect(0, 0, self.game.arena.playfield_size, self.game.arena.playfield_size), )


        # Draw animation of player
        self.previous_player_pos.get()
        self.previous_player_pos.put(self.game.arena.player.position)

        for i in range(len(self.previous_player_pos.queue)):
            multiplier = max((i / (2 * len(self.previous_player_pos.queue))) - 0.25, 0)
            surf = pygame.Surface((self.game.arena.player.radius * 2, self.game.arena.player.radius * 2))
            surf.set_colorkey((0, 0, 0))
            surf.set_alpha(int(multiplier * 255))

            pos = self.previous_player_pos.queue[i]
            rad = self.game.arena.player.radius

            pygame.draw.circle(surf, self.trail_color, (surf.get_size()[0]/2, surf.get_size()[1]/2), rad)

            self.screen.blit(surf, (pos[1]-rad, pos[0]-rad))

        # Draw player
        pygame.draw.circle(self.screen, self.game.arena.player.color, self.game.arena.player.position[::-1], self.game.arena.player.radius)

        # Draw enemies, obstacles and win circles
        for obstacle in self.game.arena.obstacles:
            pygame.draw.circle(self.screen, obstacle.color, obstacle.position[::-1], obstacle.radius)
        for enemy in self.game.arena.homing_enemies:
            pygame.draw.circle(self.screen, enemy.color, enemy.position[::-1], enemy.radius)
        for win in self.game.arena.win_circles:
            pygame.draw.circle(self.screen, win.color, win.position[::-1], win.radius)

        # Draw points
        self.screen.blit(points_surface, (0, 0))
        self.screen.blit(max_points_surface, (0, 40))

        pygame.display.flip()