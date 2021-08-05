import random

from CircleGame import circles as cr


class Arena:

    def gen_circle_anywhere(self, color, max_speed, min_radius, max_radius):
        circle = cr.Circle()
        circle.position = (random.randint(0, self.playfield_size), random.randint(0, self.playfield_size))
        circle.radius = random.randint(min_radius, max(min_radius, max_radius))
        circle.color = color
        circle.max_speed = max_speed
        return circle

    def __init__(self, obstacle_count, homing_enemy_count, speed=1.0):
        self.playfield_size = random.randint(700, 1000)
        self.player = cr.Circle((15, self.playfield_size // 2), random.randint(10, 15), (100, 250, 255), random.randint(250, 300)*speed)
        self.obstacles = []
        self.win_circles = []
        self.time_left = 5

        homing_enemy_count = min(homing_enemy_count, 30)
        obstacle_count = min(obstacle_count, 20)

        for i in range(obstacle_count):
            while True:
                circle = self.gen_circle_anywhere((200, 0, 0), 0, 20, self.playfield_size // (obstacle_count*3 + 4))
                if not circle.within_range(self.player, 5):
                    self.obstacles.append(circle)
                    break

        self.homing_enemies = []
        for i in range(homing_enemy_count):
            while True:
                circle = self.gen_circle_anywhere((220, 0, 128), random.randint(150, 225)*speed, 20, self.playfield_size // (homing_enemy_count*2 + 10))
                if not circle.within_range(self.player, 25):
                    self.homing_enemies.append(circle)
                    break

        for i in range(3):
            while True:
                circle = self.gen_circle_anywhere((0, 240, 0), random.randint(30, 45), 20, 40)
                if not circle.within_range(self.player, 5):
                    self.win_circles.append(circle)
                    break

    def _contain_circle(self, circle):
        x = circle.position[0]
        y = circle.position[1]
        if x > self.playfield_size:
            x = self.playfield_size
        elif x < 0:
            x = 0

        if y > self.playfield_size:
            y = self.playfield_size
        elif y < 0:
            y = 0

        circle.position = (x, y)

    def _contain_all_objects(self):
        self._contain_circle(self.player)
        for enemy in self.homing_enemies:
            self._contain_circle(enemy)
        for obstable in self.obstacles:
            self._contain_circle(obstable)

    def update(self, dt, controller):
        x_input, y_input = controller.get_axis_vals()
        self.player.move_by(dt * x_input, dt * y_input)

        self.time_left -= dt

        for enemy in self.homing_enemies:
            delta_x = self.player.position[0] - enemy.position[0]
            delta_y = self.player.position[1] - enemy.position[1]
            length = (delta_x**2 + delta_y**2)**0.5
            if length != 0 and length > 1:
                delta_x /= length
                delta_y /= length
            enemy.move_by(dt * delta_x, dt * delta_y)

        self._contain_all_objects()

    def is_win(self):
        if not self.is_lost():
            for win in self.win_circles:
                if win.collides(self.player):
                    return True
        return False

    def is_lost(self):
        for obstacle in self.obstacles:
            if obstacle.collides(self.player):
                return True
        for enemy in self.homing_enemies:
            if enemy.collides(self.player):
                return True
        if self.time_left <= 0:
            return True
        return False
